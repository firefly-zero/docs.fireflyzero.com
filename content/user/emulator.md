---
title: Emulator
weight: 10
params:
  art: /emulator.png
  icon: fa-solid fa-computer
  emoji: 💻
---

The emulator allows you to run any Firefly Zero apps on your computer. To install it, follow the [Installation]({{< ref "installation.md" >}}) guide.

## 🕹 Input

The emulator supports the following input methods, from best to worst.

1. Firefly Zero device
1. Steam controller
1. Gamepad
1. (⌛ Coming soon) UI buttons
1. Keyboard

### 📱 Firefly Zero device

The device can be used as a gamepad (not only for the emulator). See [firefly-gamepad](https://github.com/firefly-zero/firefly-gamepad).

### 💨 Steam controller

It is discontinued but you may find a used one. It has a touchpad just like Firefly Zero, and that makes it a better fit, compared to Xbox controllers, for apps requiring a precise input.

The controls are the same as for any other gamepad. See the next section.

### 🎮 Gamepad

* The buttons (`A`, `B`, `X`, and `Y`) map to the buttons in the same position on the device.
* The `start` button on the controller does the same as `menu` on the device.
* The touch pad is emulated by the left stick. The input from the stick is read only if you press the `LB` (left shoulder button). This is because unlike touch pad, the stick is always active, even in the resting state.

If you have multiple gamepads connected, the emulator will pick the one from which it receives the first input. So, if you want to run multiple emulators with multiple gamepads (to play multiplayer games), do the following:

1. Launch the first emulator.
1. Press any button on the first gamepad.
1. Launch the second emulator.
1. Press any button on the second gamepad.

### 🖱 UI buttons

(⌛ Coming soon)

### ⌨️ Keyboard

Keyboard is quite far from how inputs work on the device. It doesn't have a touchpad. The controls are the following:

1. `Esc`: close the emulator
1. `Z` or `Space`: S
1. `X` or `Enter`: E
1. `A` or `Backspace`: W
1. `S`: N
1. `Tab`: menu
1. `←` or `4`: touchpad left
1. `→` or `6`: touchpad right
1. `↑` or `8`: touchpad up
1. `↓` or `2`: touchpad down
1. `5`: touchpad middle

{{< hint info >}}
**How to remember this?**

Rotate the keyboard 45° counterclockwise. The bottom left corner of your keyboard (ZXAS) forms the crosshair of the buttons as they are on the device (SEWN).

![layot example](/keyboard.png)

{{< /hint >}}

If you run multiple emulators, the keyboard input is read by the one that has the window focus. Press `Alt+Tab` to switch the focus.
