---
title: 🎮 Input
weight: 20
---

The `read_buttons` function returns which buttons are currently pressed. The SDKs also provide convenience methods to compare two states to get which buttons were just pressed or just released.

The function requires a `Peer` argument. It defines which input should be read in multiplayer and is covered in more details on the [Multiplayer](./net.md) page. For a simple single-player game, you can ask it for a combined input from all devices (which is in a single-player game just the input from a single device):

{{< tabs "read-buttons" >}}
{{< tab "🦀 Rust" >}}

```rust
use firefly_rust::*;
let buttons = read_buttons(Peer::COMBINED);
```

{{< /tab >}}
{{< tab "🏃 Go" >}}

```go
buttons := firefly.ReadButtons(firefly.Combined)
```

{{< /tab >}}
{{< /tabs >}}

## Touch pad

The `read_pad` function returns the coordinates of the finger on the touch pad if user currently presses it. The coordinates are expressed as a pair of X and Y values in the range from -1000 to 1000 (both ends included). SDKs also provide a way to convert it into [polar coordinates](https://en.wikipedia.org/wiki/Polar_coordinate_system) using `radius` and `azimuth` methods.

{{< tabs "read-pad" >}}
{{< tab "🦀 Rust" >}}

```rust
use firefly_rust::*;
let pad = read_pad(Peer::COMBINED);
if let Some(pad) = pad {
    todo!()
}
```

{{< /tab >}}
{{< tab "🏃 Go" >}}

```go
pad, pressed := firefly.ReadPad(firefly.Combined)
if pressed {
    // ...
}
```

{{< /tab >}}
{{< /tabs >}}

When using the emulator with a gamepad, you have to press the stick down (or press LB) for the input to be recognized. This is because we need a way to distinguish between not touching the touch pad and touching it in the middle.

{{< button relref="./net.md" >}}➡️ Multiplayer{{< /button >}}
