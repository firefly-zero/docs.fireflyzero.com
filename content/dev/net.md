---
title: Multiplayer
weight: 22
params:
  art: /multiplayer.png
  icon: fa-solid fa-wifi
  emoji: 🔃
---

Firefly Zero has a very unique approach to multiplayer: every game (or app) can be played together! The only question is how the app handles multiple inputs. And this section covers how you can do that. And don't worry, it's very simple.

## ⚙️ How it works

If you take two or more calculators and punch into all of them the same expression, you'll get the same result. However if you make a typo in any of them, the result might be very different.

And that's exactly how Firefly Zero works: all connected devices agree on the same environment for the startup and each update. They synchronize their random values, system time, all the inputs, when to render each frame, etc. The only things that your app need to worry about is what inputs you use and what files you read.

## 🎮 Handling inputs

There are two ways to handle user input: you can either read the combined input from all devices in one go or read each input separately.

The easiest option is to read the combined input from all devices. This is the best strategy for the apps designed to be played alone. If there is only one device (aka peer), the result will be the input from that device. And if there are multiple devices connected, the result will be the combined input from all devices: if anyone presses a button, it is reported as pressed.

{{< tabs >}}
{{< tab "Rust" >}}

```rust
use firefly_rust::*;
let pad = read_pad(Peer::COMBINED);
let buttons = read_buttons(Peer::COMBINED);
```

{{< /tab >}}
{{< tab "Go" >}}

```go
pad, pressed := firefly.ReadPad(firefly.Combined)
buttons := firefly.ReadButtons(firefly.Combined)
```

{{< /tab >}}
{{< tab "C/C++" >}}

```c
Pad pad = read_pad(COMBINED);
Buttons buttons = read_buttons(COMBINED);
```

{{< /tab >}}
{{< /tabs >}}

The second option is to read and handle each input individually. This is the best option for when you want to provide a custom logic for multiplayer.

{{< tabs >}}
{{< tab "Rust" >}}

```rust
use firefly_rust::*;
let peers = get_peers();
for peer in peers {
    let pad = read_pad(peer);
    let buttons = read_buttons(peer);
    todo!();
}
```

{{< /tab >}}
{{< tab "Go" >}}

```go
peers := firefly.GetPeers()
for _, peer := range peers.Slice() {
    pad, pressed := firefly.ReadPad(peer)
    buttons := firefly.ReadButtons(peer)
    // ...
}
```

{{< /tab >}}
{{< tab "C/C++" >}}

```c
Peers peers = get_peers()
Peer peer;
for (peer = 0; peer < 32; peer++) {
    if (is_online(peer)) {
        Pad pad = read_pad(peer);
        Buttons buttons = read_buttons(peer);
        // ...
    }
}
```

{{< /tab >}}
{{< /tabs >}}

## 💾 Handling files

Since all devices run the same app, all files in the ROM are the same, so reading them on every device will give the same result.

Things are a bit trickier with data files. In a future release of the emulator, there will be a way to provide files that are synchronized over the network. For now, all data files are local to each device. So, the best approach is to not use them if there is more than one peer connected. Or use in a way that doesn't impact the gameplay (for example, to remember the user's preferred color scheme).

## 🙋 Local peer

You can call the `get_me` function to get the `Peer` corresponding to the local device. But be careful! Do not let it affect the game logic. Otherwise, the state of the app will be different on every device, and everyone will be playing a different game. Use it only for visual effects, like a marker showing the player which character is their. Or showing them only their score. Or in a hidden agenda game (like Mafia) showing them only their role.

{{< tabs >}}
{{< tab "Rust" >}}

```rust
use firefly_rust::*;
let peers = get_peers();
let me = get_me();
for peer in peers {
    if peer == me {
        todo!()
    }
}
```

{{< /tab >}}
{{< tab "Go" >}}

```go
peers := firefly.GetPeers()
me := firefly.GetMe()
for _, peer := range peers.Slice() {
    if peer == me {
        // ...
    }
}
```

{{< /tab >}}
{{< tab "C/C++" >}}

```c
Peers peers = get_peers();
Peer me = get_me();
for (peer = 0; peer < 32; peer++) {
    if (is_online(peer) && peer == me) {
        // ...
    }
}
```

{{< /tab >}}
{{< /tabs >}}

## 🥇 Peers' order

The peers are sorted based on their MAC address. That means, the same devices connected together always go in the same order. That also means, if you always give the same peer (for example, the first one on the list) a game advantage (like going first in chess), the same player will always have that advantage. To make things fair, pick a random starting player for each game session using the `get_random` function.

{{< tabs >}}
{{< tab "Rust" >}}

```rust
use firefly_rust::*;
let peers = get_peers();
let idx = get_random() % peers.len();
let peer = peers.iter().nth(idx).unwrap();
```

{{< /tab >}}
{{< tab "Go" >}}

```go
peers := firefly.GetPeers()
idx := firefly.GetRandom() % peers.Len()
peer := peers.Slice()[idx]
```

{{< /tab >}}
{{< tab "C/C++" >}}

```c
Peer peers = get_peers();
// TODO
```

{{< /tab >}}
{{< /tabs >}}
