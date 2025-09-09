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

The function requires a `Peer` argument. It defines which input should be read in multiplayer and is covered in more details on the [Multiplayer](https://docs.fireflyzero.com/dev/net/) page. For a simple single-player game, you can ask it for a combined input from all devices (which is in a single-player game just the input from a single device):

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
