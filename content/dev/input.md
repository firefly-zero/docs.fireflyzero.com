---
title: Input
weight: 20
params:
  art: /input.png
  icon: fa-solid fa-gamepad
  emoji: 🎮
---

## Buttons

> Just feel that you're the hardest little button to button.

Firefly Zero has 4 primary buttons:

* `N` (North) on the top.
* `S` (South) on the bottom.
* `W` (West) on the left.
* `E` (East) on the right.

There are also Menu and Power buttons but regular apps don't have access to these.

The `read_buttons` function returns which buttons are currently pressed. The SDKs also provide convenience methods to compare two states to get which buttons were just pressed or just released.

The function requires a `Peer` argument. It defines which input should be read in multiplayer and is covered in more details on the [Multiplayer]({{< ref "/dev/net/" >}}) page. For a simple single-player game, you can ask it for a combined input from all devices (which is in a single-player game just the input from a single device):

{{< tabs >}}
{{< tab "Rust" >}}

```rust
use firefly_rust::*;
let buttons = read_buttons(Peer::COMBINED);
```

{{< /tab >}}
{{< tab "Go" >}}

```go
buttons := firefly.ReadButtons(firefly.Combined)
```

{{< /tab >}}
{{< tab "Zig" >}}

```zig
const buttons = ff.readButtons(ff.Peer.combined);
```

{{< /tab >}}
{{< tab "C/C++" >}}

```c
Buttons buttons = read_buttons(COMBINED);
```

{{< /tab >}}
{{< /tabs >}}

## Buttons best practice

> The only thing better than perfect is standardized.

We recommend the following mapping:

* `E`: attack, accept, ok, select, interact, next list item.
* `W`: cancel, back, exit, previous list item.
* `S`: jump, crawl.
* `N`: alt attack, open inventory, open map, open in-game menu.

In general, we expect sequences go from left to right. For example, a sequence of numbers (from smaller to bigger) or a timeline (from past to future). That means, going to the next item or screen will be the right button (`E`) and going back to the previous item or screen will the the left one (`W`).

For vertical controls, it's typically from bottom to top. For example, horizontal sound controls would go from silent on the left to loud on the right and vertical sound controls would go from silent on the bottom to loud on the top.

There are quite a few variations between different game platforms, both cultural and historical. You can see `A` on the left and `B` on the right, `A` on the bottom and `B` on the right, or `B` on the bottom and `A` on the right. For platforms with `A` on the bottom and `B` on the right, Eastern countries will use `B` for confirmation (because of the reasons above, although the traditional "tategaki" Japaneese is written from right to left) but Western countries will use `A` for it ("A" for "Accept" in English). It might be a good idea to remap controls to match Firefly Zero conventions but make sure that it is consistent within the app and matches the game UI.

Providing consistent controls within all apps on the platform is a good UX, that's why we write this guideline. However, if you have reasons to believe a different control scheme would fit your game better, go for it! We're all here to have fun, so we will always take creativity over rules.

## Touch pad

> 'Cause every time we touch, I feel the static.

The touch pad is located on the left side of the device and controlled by the left thumb. It doesn't support multi-touch or pressure detection.

The `read_pad` function returns the coordinates of the finger on the touch pad if user currently presses it. The coordinates are expressed as a pair of X and Y values in the range from -1000 to 1000 (both ends included). SDKs also provide a way to convert it into [polar coordinates](https://en.wikipedia.org/wiki/Polar_coordinate_system) using `radius` and `azimuth` methods.

{{< tabs >}}
{{< tab "Rust" >}}

```rust
use firefly_rust::*;
let pad = read_pad(Peer::COMBINED);
if let Some(pad) = pad {
    todo!()
}
```

{{< /tab >}}
{{< tab "Go" >}}

```go
pad, pressed := firefly.ReadPad(firefly.Combined)
if pressed {
    // ...
}
```

{{< /tab >}}
{{< tab "Zig" >}}

```zig
const maybePad = ff.readPad(ff.Peer.combined);
if (maybePad) |pad| {
    // ...
}
```

{{< /tab >}}
{{< tab "C/C++" >}}

```c
Pad pad = read_pad(COMBINED);
if (pad.touched)
{
    // ...
}
```

{{< /tab >}}
{{< /tabs >}}

When using the emulator with a gamepad, you have to press the stick down (or press LB) for the input to be recognized. This is because we need a way to distinguish between not touching the touch pad and touching it in the middle.

## Touch pad best practice

> If you put a large switch in some cave somewhere, with a sign on it saying "End-of-the-World Switch. PLEASE DO NOT TOUCH", the paint wouldn't even have time to dry.

Everyone is familiar with touch screens. Most gamers are also familiar with sticks (as on most of gamepads) and DPad (as also on gamepads, albeit rarely used, and on retro game consoles). Touch pad, even though it's present on every laptop, takes some time to get familiar with, especially in the context of gaming. It's a quick adjustment but an adjustment nonetheless. Hence we can divide apps into two categories:

1. Games and apps pre-installed on the device. These are the apps the newcomer tries first and hence they should be resilient, support all possible behaviors, but also teach the user how to use the touchpad the best.
1. Games and apps explicitly installed by the user. These apps may assume that the user is already familiar with the device. In case the input is different from the pre-installed apps, it's a good to include in the app description in the catalog some info on how to use it. And, if possible, an in-app tutorial is always a good idea.

Depending on how you want your app feel, there are some common patterns on reading the input:

1. **Radial angle**. You read from the touchpad the movement direction, shooting direction, or another direction. The adjustment of the direction can be immediate (as in [Through the gate](https://catalog.fireflyzero.com/lux.gates)) or gradual (like in [Snek](https://catalog.fireflyzero.com/lux.snek)). This is especially useful when porting crank-centric Playdate games. To read the angle, most SDKs provide `Pad.azimuth` method.
1. **Angle and radius**. In addition to the angle, you might also want to detect the distance from the touchpad center to the touch point. For example, to adjust the character movement in the direction (from walking to running). To read that distance, most SDKs provide `Pad.radius` method.
1. **Coordinate changes**. When the user presses the touchpad, you calculate the new position relative to the previous touch position. In other words, when player just touches the touchpad, nothing happens. Then if they move the finger to the left, the character in the game also moves to the left. And the movement speed in the game correlates with the finger movement speed. It is used in games where precise movement is needed (like [Shoot!](https://catalog.fireflyzero.com/lux.shoot)) or in drawing apps. It's a very intuitive input method and most newcomers don't have problems figuring it out. However, it requires from the game a very good collision detection. Coordinates is how the `read_pad` function returns the data, all you need to do is to access the `Pad.x` and `Pad.y` attributes.
1. **Swiping**. Swiping works just like coordinate changes except that when the touchpad is released, you want to keep the inertia (maybe slowing it down over time). So, if I touch the pad on the right, quickly move my finger to the left, and release the pad without slowing down, the character (or whatever is controlled by the pad) should keep moving to the left. It doesn't make much sense for games but it's good for navigating through long lists of items (like going through cards in deck-building games).
1. **DPad** (directional pad). Sometimes you just want to know if it is up, down, left, or right. And sometimes maybe also diagonal movements too (upper-right, lower-left, etc). This is useful for games on square grid (like [Blutti](https://catalog.fireflyzero.com/olle.blutti)) and also for porting retro games designed for DPad. For this purpose, the SDKs provide `DPad` type which can be produced from `Pad` (by type-casting, `as_dpad` method, `to_dpad` method, or whatever is convention in the used programming language).

Many new players use the touchpad like a stick: putting their finger in the middle and then sliding it in the direction they want to move. This is why in all SDKs, when you convert `Pad` into `DPad`, there is a dead zone in the middle where we don't consider the touch to be in any specific direction.
