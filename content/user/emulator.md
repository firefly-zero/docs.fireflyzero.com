---
title: 💻 Emulator
weight: 5
params:
  art: /emulator.png
---

## 📥 Installation

1. [Download emulator binary](https://github.com/firefly-zero/firefly-emulator-bin/releases) and put it into `$PATH`.
1. Install [firefly-cli](https://github.com/firefly-zero/firefly-cli): `cargo install firefly_cli`
1. Install a game: `firefly_cli import lux.snek`
1. Run `firefly_emulator`.

## 🕹 Input

The emulator supports the following input methods, from best to worst.

1. (⌛ Coming soon) Firefly Zero device
1. Steam controller
1. Gamepad
1. (⌛ Coming soon) UI buttons
1. Keyboard

### 📱 Firefly Zero device

(⌛ Coming soon)

### 💨 Steam controller

It is discontinued but you may find a used one. It has a touchpad just like Firefly Zero, and that makes it a better fit, compared to Xbox controllers, for apps requiring a precise input.

The controls are the same as for any other gamepad. See the next section.

### 🎮 Gamepad

* The buttons (`A`, `B`, `X`, and `Y`) are the same and work the same as on the actual device.
* The `start` button on the controller does the same as `menu` on the device.
* The touch pad is emulated by the left stick. The input from the stick is read only if you press the `LB` (left shoulder button). This is because unlike touch pad, the stick is always active, even in the resting state.

### 🖱 UI buttons

(⌛ Coming soon)

### ⌨️ Keyboard

Keyboard is quite far from how inputs work on the device. It doesn't have a touchpad. The controls are the following:

1. `Esc`: close the emulator
1. `Z`, `Enter`, or `Space`: A
1. `X`, `B`, or `Backspace`: B
1. `A`: X
1. `S` or `Y`: Y
1. `Tab`: menu
1. `←` or `4`: touchpad left
1. `→` or `6`: touchpad right
1. `↑` or `8`: touchpad up
1. `↓` or `2`: touchpad down
1. `5`: touchpad middle
