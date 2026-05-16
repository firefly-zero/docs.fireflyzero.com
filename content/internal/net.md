---
title: Multiplayer
weight: 55
params:
  icon: fa-solid fa-wifi
  emoji: 🛜
---

## Protocol

Multiplayer on Firefly Zero devices uses [esp-now](https://www.espressif.com/en/solutions/low-power-solutions/esp-now) (see also: [tech docs](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/network/esp_now.html)). It is a peer-to-peer communication protocol that uses WiFi frequency (13.56 Ghz). It comes out-of-the-box on ESP32 chips which are the chips that we use. The main reasons for choosing esp-now over WiFi or Bluetooth are performance and simplicity (which are connected). It also has a very basic encryption and delivery confirmations (which we use for retries).

The messages are exchanged directly by all peers. There is no leader. In 4-player multiplayer, each device will send messages to all 3 other devices and receive messages from all of them.

Messages are serialized using [Postcard](https://postcard.jamesmunns.com/wire-format) Rust library. The message payload is defined in the [`net/message.rs`](https://github.com/firefly-zero/firefly-runtime/blob/main/src/net/message.rs) file in [firefly-runtime](https://github.com/firefly-zero/firefly-runtime). Every message is sent as a single esp-now packet, so it must fit 250 bytes. Also, bigger packets have a higher chance of being corrupted and discarded ("lost").

## Hardware

We use 2 ESP32 chips: firefly-main and firefly-io. The former is the main runtime and the latter handles networking. The reasons for two chips are:

1. WiFi and esp-now stacks require a lot of resources.
1. We want to run it on a separate core but both cores on the main device are busy (with main logic and with audio).
1. One chip doesn't have enough pins to connect all peripherals. Only display alone takes more than 20 GPIO pins.

## States

Networking is represented as one of 4 states:

1. `None`. Single-player mode. The WiFi chip is powered off to save energy.
1. `Connector`. The device is running `sys.connector`. The device is announcing itself, listening for other devices, and exchanging `Intro` packets. Every device must go through 2 stages of registration to be recognized by another device: to be registered in esp-now manager with `HELLO` message and to be registered in Firefly Zero runtime with the `Intro` message.
1. `Connection`. The connection to all other perrs is established, no new connections are accepted. This is the state in which the devices are in the launcher. The transition to the next state is done with the `Start` message which is emitted when an app is launched.
1. `FrameSyncer`. The devices are running an app. Every frame, they exchange the `FrameState` packets. They are very small and contain only input, random seed, and sometimes an action requested by the peer (restart or exit the app). The device will not transition to the next frame until it receives the corresponding frame states from all devices. Another thing to note is that there is no such thing as "at the same time" in distributed systems: one device may update the frame sooner than another if it receives all states earlier. The drift won't go beyond 1-2 frames, though: if the device lags behind, it will delay it's outgoing frame state messages, delaying all other devices. It's also possible to receive a frame state for N+1 frame before N frame, so frames are stored in a small ring buffer.

The last message is `Disconnect` which indicates that the device has disconnected. It may or may not cause the state transition but it always at least removes the peer from the peers list.

In reality, there are more "sub-" states (mostly for delivery guarantees and error handling). However, implementing a proper state machine in low-level Rust proved to be difficult and costly. A 4-state model might be a bit messier and more repetitive but it works and is very fast for the most common "happy path" scenarios.

## Emulator

Networking in emulator is implemented using UDP. By default, each emulator tries to pick the first available UDP port in a hardcoded range and then sends advertisements to all ports in the same range to find the other emulators. This behavior can be controlled by `--udp-ip` and `--peers` flags. In particular, to connect over local network emulators running on different computers.

Since there is no desktop implementation of esp-now protocol for desktop (which would require not only a good deal of reverse engineering but also low-level ("monitor mode") to the WiFi chip), an emulator cannot be connected to a device.
