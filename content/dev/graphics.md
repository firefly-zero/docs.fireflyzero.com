---
title: Graphics
weight: 15
params:
  art: /graphics.png
  icon: fa-solid fa-palette
  emoji: 🎨
---

## 🔬 Pixels

The screen size 240x160 pixels, just like GameBoy Advance. Pixels are quite big, so it's safe to draw one pixel wide lines and letters, they will be visible.

Coordinates: x=0 is left, x=240 is right, y=0 is top, and y=160 is bottom.

## 🖼 Frames

> All those moments will be lost in time.

Each update of the image on the screen is called "frame". Before each frame is rendered, the `render` callback function is called. This is where you should call all drawing functions you need.

Don't draw from the `update` callback: while `update` is called ~60 times per second, `render` might be called less often if there are not enough resources. So, if you draw from `update`, you'll waste resources on updating a frame that will be never rendered on the screen.

The frame that you had at the previous update is not cleared. So, if only a small region on the screen needs to be changed, you can redraw only that region and leave the rest intact. If it's not what you want and you'd prefer to redraw the whole frame each time, call `clear_screen`, and it will fill the whole frame with the color you specified.

## 🎨 Colors

> The enemy of art is the absence of limitations.

Each frame is stored in memory as one of 16 shades of gray. When the time comes to draw the frame on the screen, each of these shades is mapped to one of 16 colors in the color palette.

The default color palette is [Sweetie 16](https://lospec.com/palette-list/sweetie-16):

{{< hint warning >}}

If you use Dark Reader extension in your browser, make sure to turn it off when viewing the palette below. Otherwise, you'll see incorrect colors!

{{< /hint >}}

1. <span style="background-color: #1a1c2c; min-width: 40px; height: 1em; display: inline-block"></span> #1A1C2C: `Black`
1. <span style="background-color: #5d275d; min-width: 40px; height: 1em; display: inline-block"></span> #5D275D: `Purple`
1. <span style="background-color: #b13e53; min-width: 40px; height: 1em; display: inline-block"></span> #B13E53: `Red`
1. <span style="background-color: #ef7d57; min-width: 40px; height: 1em; display: inline-block"></span> #EF7D57: `Orange`
1. <span style="background-color: #ffcd75; min-width: 40px; height: 1em; display: inline-block"></span> #FFCD75: `Yellow`
1. <span style="background-color: #a7f070; min-width: 40px; height: 1em; display: inline-block"></span> #A7F070: `LightGreen`
1. <span style="background-color: #38b764; min-width: 40px; height: 1em; display: inline-block"></span> #38B764: `Green`
1. <span style="background-color: #257179; min-width: 40px; height: 1em; display: inline-block"></span> #257179: `DarkGreen`
1. <span style="background-color: #29366f; min-width: 40px; height: 1em; display: inline-block"></span> #29366F: `DarkBlue`
1. <span style="background-color: #3b5dc9; min-width: 40px; height: 1em; display: inline-block"></span> #3B5DC9: `Blue`
1. <span style="background-color: #41a6f6; min-width: 40px; height: 1em; display: inline-block"></span> #41A6F6: `LightBlue`
1. <span style="background-color: #73eff7; min-width: 40px; height: 1em; display: inline-block"></span> #73EFF7: `Cyan`
1. <span style="background-color: #f4f4f4; min-width: 40px; height: 1em; display: inline-block"></span> #F4F4F4: `White`
1. <span style="background-color: #94b0c2; min-width: 40px; height: 1em; display: inline-block"></span> #94B0C2: `LightGray`
1. <span style="background-color: #566c86; min-width: 40px; height: 1em; display: inline-block"></span> #566C86: `Gray`
1. <span style="background-color: #333c57; min-width: 40px; height: 1em; display: inline-block"></span> #333C57: `DarkGray`

You can modify colors in the palette by calling the `set_color` function:

{{< tabs >}}
{{< tab "Rust" >}}

```rust
use firefly_rust::*;
set_color(
    Color::Red,
    RGB{r: 0xff, g: 0x00, b: 0x00},
);
```

{{< /tab >}}
{{< tab "Go" >}}

```go
firefly.SetColor(
    firefly.ColorRed,
    firefly.RGB{R: 0xff, G: 0x00, B: 0x00},
);
```

{{< /tab >}}
{{< tab "Zig" >}}

```zig
const ff = @import("firefly");
ff.setColor(
    ff.Color.red,
    ff.RGB{.r = 0xff, .g = 0x00, .b = 0x00},
);
```

{{< /tab >}}
{{< tab "C/C++" >}}

```c
#include "./vendor/firefly/firefly.c"
RGB color = {.r = 0xff, .g = 0x00, .b = 0x00};
set_color(RED, color);
```

{{< /tab >}}
{{< /tabs >}}

Looking for inspiration? Check out [lospec.com](https://lospec.com/palette-list/) for nice-looking color palettes.

## 🌈 More colors

It is possible to render more than 16 colors on a single frame. First, you need to divide the elements on the screen to horizontal regions:

... (TODO: add an image with an example)

Then you can provide a `render_line` callback function. The callback accepts the line for each it is called and returns the next line before which it should be called again. For example, it is called with 0 first time and if it then returns 100, it will be called again before rendering the line 100. If then it returns 0, it will be called again only when rendering the next frame.

This callback must be as fast as possible and all it should do is change the colors in the palette. In other words, the callback can be used to swap the colors in the palette on the go, as lines are rendered on the screen.

## 🔳 Shapes

> It is the sculptor's power, so often alluded to, of finding the perfect form and features of a goddess, in the shapeless block of marble.

The runtime provides a bunch of functions that you can call to draw primitive shapes and lines. All these functions follow the same rules:

1. The first argument is usually the coordinate of the upper-left corner of the bounding box in which the shape should be drawn (`Point`). Coordinates might point outside of the screen (including being negative). In that case, only the shape parts that are within the screen boundaries will be drawn.
1. The second argument is usually the size of the bounding box (`Size`). Both width and height must be positive.
1. The last argument is typically the style of the shape (`Style`): fill color, stroke color, and stroke width. The exception are `draw_point`, which accepts only one color, and `draw_line`, which doesn't need the fill color.

For a reference, here is the list of available functions for drawing shapes:

1. `draw_point(👉 Point, 📦 Size, 💄 Color)`
1. `draw_line(👉 Point, 📦 Size, 💄 LineStyle)`
1. `draw_rect(👉 Point, 📦 Size, 💄 Style)`
1. `draw_rounded_rect(👉 Point, 📦 Size, 📦 Size, 💄 Style)`
1. `draw_circle(👉 Point, ⭕ Diameter, 💄 Style)`
1. `draw_ellipse(👉 Point, 📦 Size, 💄 Style)`
1. `draw_triangle(👉 Point, 👉 Point, 👉 Point, 💄 Style)`
1. `draw_arc(👉 Point, ⭕ Diameter, 📐 Angle, 📐 Angle, 💄 Style)`
1. `draw_sector(👉 Point, ⭕ Diameter, 📐 Angle, 📐 Angle, 💄 Style)`

{{< tabs >}}
{{< tab "Rust" >}}

```rust
use firefly_rust::*;
draw_triangle(
    Point { x: 60, y: 10 },
    Point { x: 40, y: 40 },
    Point { x: 80, y: 40 },
    Style {
        fill_color: Color::LightGray,
        stroke_color: Color::DarkBlue,
        stroke_width: 1,
    },
);
```

{{< /tab >}}
{{< tab "Go" >}}

```go
firefly.DrawTriangle(
    firefly.Point{X: 60, Y: 10},
    firefly.Point{X: 40, Y: 40},
    firefly.Point{X: 80, Y: 40},
    firefly.Style{
        FillColor:   firefly.ColorDarkBlue,
        StrokeColor: firefly.ColorBlue,
        StrokeWidth: 1,
    },
)
```

{{< /tab >}}
{{< tab "Zig" >}}

```zig
const ff = @import("firefly");
ff.drawTriangle(
    ff.Point{ .x = 60, .y = 10 },
    ff.Point{ .x = 40, .y = 40 },
    ff.Point{ .x = 80, .y = 40 },
    ff.Style{
        .fill_color = ff.Color.light_gray,
        .stroke_color = ff.Color.dark_blue,
        .stroke_width = 1,
    },
);
```

{{< /tab >}}
{{< tab "C" >}}

```c
Point p1 = {60, 10};
Point p2 = {40, 40};
Point p3 = {80, 40};
Style s = {
    .fill_color = LIGHT_GRAY,
    .stroke_color = DARK_BLUE,
    .stroke_width = 1};
draw_triangle(p1, p2, p3, s);
```

{{< /tab >}}
{{< tab "C++" >}}

```c++
draw_triangle(
    {60, 10}, {40, 40}, {80, 40},
    {
        .fill_color = LIGHT_GRAY,
        .stroke_color = DARK_BLUE,
        .stroke_width = 1,
    });
```

{{< /tab >}}
{{< /tabs >}}

## 📸 Images

> A picture is worth a thousand words.

Draw the image you want using the default ([Sweetie 16](https://lospec.com/palette-list/sweetie-16)) color palette. You can also use a transparent background. Save the image as a PNG file.

{{< hint info >}}

[Lospec Pixel Editor](https://apps.lospec.com/pixel-editor/) is a good online editor for pixel art. On the left panel, specify the image size you want, select "Sweetie 16" as the color palette, and press "Create". Draw your art, press "File" and then "Export".

{{< /hint >}}

Link the saved file in `firefly.toml`:

```toml
[files]
img = { path = "image.png" }
```

Where `img` is the name of the image in the ROM.

Next, load the image from ROM into the memory:

{{< tabs >}}
{{< tab "Rust" >}}

```rust
let file = firefly_rust::load_buf("img");
```

{{< /tab >}}
{{< tab "Go" >}}

```go
file := firefly.LoadFile("img", nil);
```

{{< /tab >}}
{{< tab "Zig" >}}

```zig
const file = ff.loadFile("img");
```

{{< /tab >}}
{{< tab "C/C++" >}}

```c
// We know the image size in advance.
// You can see it when running `firefly_cli build`.
// You could also use `get_file_size` to detect the file size
// in runtime but that requires using an allocator.
const size_t fileSize = 97;
char head[fileSize];
Buffer buf = {.head = head, .size = fileSize};
image = load_file("img", buf);
```

{{< /tab >}}
{{< /tabs >}}

Lastly, call `draw_image` with the image you loaded earlier.

## 🔤 Text

First, go to [fonts.fireflyzero.com](https://fonts.fireflyzero.com/) and download the font that you'd like to use. Then add it into `firefly.toml` as you add images:

```toml
[files]
font = { path = "eg_6x9.fff" }
```

Now you can load the font from ROM as you load images and call `draw_text` with the text you want to render and the font.

The text does not automatically wrap. If you need word wrapping, you should add new lines into the text yourself.

## 🖌 Canvas

Canvas is an image in memory that you can draw on. It is useful for drawing from scratch some complex images that should be persisted between multiple frames. For example, it can dirt on a character, bullet marks on walls, debries on the ground, randomly generated terrain, etc.

After you create a canvas and call `set_canvas`, all almost drawing functions will draw on the canvas instead of the frame buffer. And when you call `unset_canvas`, they will switch back to the frame buffer.

{{< tabs >}}
{{< tab "Rust" >}}

```rust
use firefly_zero::*;
let canvas = CanvasBuf::new(Size::new(120, 120));
set_canvas(canvas);
// fill canvas with white color
clear_screen(Color::White);
unset_canvas();
```

Just like for files, there is `Canvas`, which holds a reference, and `CanvasBuf`, which holds ownership. The latter requires the `alloc` feature to be enabled.

{{< /tab >}}
{{< tab "Go" >}}

```go
canvas := firefly.NewCanvas(firefly.Size{W: 120, H: 120})
firefly.SetCanvas(canvas)
// fill canvas with white color
firefly.ClearScreen(firefly.ColorWhite)
firefly.UnsetCanvas()
```

{{< /tab >}}
{{< tab "Zig" >}}

```zig
// TODO: Canvas not fully supported by Zig yet.
```

{{< /tab >}}
{{< tab "C/C++" >}}

```c
// TODO: Canvas not supported by C yet.
```

{{< /tab >}}
{{< /tabs >}}

{{< hint warning >}}
Currently, `draw_text`, `draw_image`, and `draw_image_sub` don't support canvas but it might change in the future. Don't call these functions when you have a canvas set!
{{< /hint >}}

To draw canvas on the screen, convert it to an image and use `draw_image`:

{{< tabs >}}
{{< tab "Rust" >}}

```rust
draw_image(canvas.as_image(), Point{ x: 10, y: 10 });
```

{{< /tab >}}
{{< tab "Go" >}}

```go
firefly.DrawImage(canvas.Image(), firefly.Point{ X: 10, Y: 10 })
```

{{< /tab >}}
{{< tab "Zig" >}}

```zig
ff.drawImage(canvas.image(), ff.Point{ .x = 10, .y = 10 })
```

{{< /tab >}}
{{< tab "C" >}}

```c
Point point = {10, 10};
draw_image(canvas, point);
```

{{< /tab >}}
{{< tab "C++" >}}

```c++
draw_image(canvas, {10, 10});
```

{{< /tab >}}
{{< /tabs >}}
