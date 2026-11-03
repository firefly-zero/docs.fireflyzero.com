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

{{< tabs >}}
{{< tab "Rust" >}}

```rust
clear_screen(Color::White);
```

{{< /tab >}}
{{< tab "Go" >}}

```go
firefly.ClearScreen(firefly.ColorWhite)
```

{{< /tab >}}
{{< tab "Zig" >}}

```zig
ff.clearScreen(.white);
```

{{< /tab >}}
{{< tab "TS" >}}

```ts
ff.clearScreen(ff.Color.White);
```

{{< /tab >}}
{{< tab "C/C++" >}}

```c
clear_screen(WHITE)
```

{{< /tab >}}
{{< tab "Odin" >}}

```odin
firefly.clear_screen(firefly.Color.White)
```

{{< /tab >}}
{{< tab "MoonBit" >}}

```moonbit
@firefly.clear_screen(White)
```

{{< /tab >}}
{{< tab "Lua" >}}

```lua
firefly.clear_screen(firefly.WHITE)
```

{{< /tab >}}
{{< /tabs >}}

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
    .red,
    .{ .r = 0xff, .g = 0x00, .b = 0x00 },
);
```

{{< /tab >}}
{{< tab "TS" >}}

```ts
import * as ff from "firefly-as/assembly";
ff.setColor(ff.Color.Red, ff.RGB.new(255, 0, 0));
```

{{< /tab >}}
{{< tab "C/C++" >}}

```c
#include "./vendor/firefly/firefly.c"
RGB color = {.r = 0xff, .g = 0x00, .b = 0x00};
set_color(RED, color);
```

{{< /tab >}}
{{< tab "Odin" >}}

```odin
color := firefly.rgb(0xff, 0x00, 0x00)
firefly.set_color(firefly.Color.Red, color)
```

{{< /tab >}}
{{< tab "MoonBit" >}}

```moonbit
@firefly.set_color(Color::Red, RGB::new(0xff, 0x00, 0x00))
```

{{< /tab >}}
{{< tab "Lua" >}}

```lua
firefly.set_color(firefly.RED, {r=0xff, g=0x00, b=0x00})
```

{{< /tab >}}
{{< /tabs >}}

See [palettes.fireflyzero.com](https://palettes.fireflyzero.com/) for the list of popular color palettes and code snippets for setting them up.

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
1. `draw_triangle(👉 Point, 👉 Point, 👉 Point, 💄 Style)`
1. `draw_circle(👉 Point, ⭕ Diameter, 💄 Style)`
1. `draw_ellipse(👉 Point, 📦 Size, 💄 Style)`
1. `draw_arc(👉 Point, ⭕ Diameter, 📐 Angle, 📐 Angle, 💄 Style)`
1. `draw_sector(👉 Point, ⭕ Diameter, 📐 Angle, 📐 Angle, 💄 Style)`

{{< tabs >}}
{{< tab "Rust" >}}

```rust
use firefly_rust::*;
draw_triangle(
    Point::new(60, 10),
    Point::new(40, 40),
    Point::new(80, 40),
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
    firefly.P(60, 10),
    firefly.P(40, 40),
    firefly.P(80, 40),
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
    .{ .x = 60, .y = 10 },
    .{ .x = 40, .y = 40 },
    .{ .x = 80, .y = 40 },
    .{
        .fill_color = .light_gray,
        .stroke_color = .dark_blue,
        .stroke_width = 1,
    },
);
```

{{< /tab >}}
{{< tab "TS" >}}

```ts
ff.drawTriangle(
    ff.Point.new(60, 10),
    ff.Point.new(40, 40),
    ff.Point.new(80, 40),
    ff.Style.new(ff.Color.LightGray, ff.Color.DarkBlue, 1)
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
{{< tab "Odin" >}}

```odin
firefly.draw_triangle(
    firefly.p(60, 10),
    firefly.p(40, 40),
    firefly.p(80, 40),
    firefly.Style {
        fill_color = firefly.Color.LightGray,
        stroke_color = firefly.Color.DarkBlue,
        stroke_width = 1,
    },
)
```

{{< /tab >}}
{{< tab "MoonBit" >}}

```moonbit
using @firefly {type Point, type Style};
@firefly.draw_triangle(
    Point::new(60, 10),
    Point::new(40, 40),
    Point::new(80, 40),
    Style::{
        fill_color: LightGray,
        stroke_color: DarkBlue,
        stroke_width: 1,
    },
);
```

{{< /tab >}}
{{< tab "Lua" >}}

```lua
firefly.draw_triangle(
    {x=60, y=10},
    {x=40, y=40},
    {x=80, y=40},
    {
        fill_color=firefly.LIGHT_GRAY,
        stroke_color=firefly.DARK_BLUE,
        stroke_width=1,
    },
)
```

{{< /tab >}}
{{< /tabs >}}

## 📸 Images

> A picture is worth a thousand words.

Draw the image you want using the default ([Sweetie 16](https://lospec.com/palette-list/sweetie-16)) color palette. You can also use a transparent background but then the maximum number of colors is limited to 15. Save the image as a PNG file.

{{< hint info >}}

Looking for a pixel art editor? Try [pixel.fireflyzero.com](https://pixel.fireflyzero.com/) or check out [Additional resources](#-additional-resources) at the end of this page.

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
let file = firefly_rust::load_file_buf("img");
let img = file.as_image();
```

{{< /tab >}}
{{< tab "Go" >}}

```go
file := firefly.LoadFile("img", nil);
img := file.Image()
```

{{< /tab >}}
{{< tab "Zig" >}}

```zig
const file = ff.loadFile("img");
const img = file.toImage();
```

{{< /tab >}}
{{< tab "TS" >}}

```ts
const file = ff.loadFile("img");
const img = file.toImage();
```

{{< /tab >}}
{{< tab "C/C++" >}}

```c
// We know the image size in advance.
// You can see it when running `ff build`.
// You could also use `get_file_size` to detect the file size
// in runtime but that requires using an allocator.
const size_t fileSize = 97;
char head[fileSize];
Buffer buf = {.head = head, .size = fileSize};
image = load_file("img", buf);
```

{{< /tab >}}
{{< tab "Odin" >}}

```odin
file := firefly.load_file_buf("img");
img := firefly.image(file)
```

{{< /tab >}}
{{< tab "MoonBit" >}}

```moonbit
let file = @firefly.load_file("img");
```

{{< /tab >}}
{{< tab "Lua" >}}

```lua
file = firefly.load_file("img");
```

{{< /tab >}}
{{< /tabs >}}

Lastly, call `draw_image` with the image you loaded earlier:

{{< tabs >}}
{{< tab "Rust" >}}

```rust
draw_image(&image, Point::new(60, 10));
```

{{< /tab >}}
{{< tab "Go" >}}

```go
firefly.DrawImage(image, firefly.P(60, 10))
```

{{< /tab >}}
{{< tab "Zig" >}}

```zig
ff.drawImage(image, .{ .x = 60, .y = 10 });
```

{{< /tab >}}
{{< tab "TS" >}}

```ts
ff.drawImage(image, ff.Point.new(60, 10));
```

{{< /tab >}}
{{< tab "C" >}}

```c
Point p = {60, 10};
draw_image(image, p);
```

{{< /tab >}}
{{< tab "C++" >}}

```c++
draw_image(image, {60, 10});
```

{{< /tab >}}
{{< tab "Odin" >}}

```odin
firefly.draw_image(image, firefly.p(60, 10))
```

{{< /tab >}}
{{< tab "MoonBit" >}}

```moonbit
@firefly.draw_image(image, Point::new(60, 10));
```

{{< /tab >}}
{{< tab "Lua" >}}

```lua
firefly.draw_image(image, {x=60, y=10})
```

{{< /tab >}}
{{< /tabs >}}

You can also select an image region using `Image.sub` and then draw it using `draw_sub_image` which is particularly useful for [tiling](#-tiling):

{{< tabs >}}
{{< tab "Rust" >}}

```rust
let sub = image.sub(Point::new(10, 10), Size::new(10, 10));
draw_sub_image(sub, Point::new(120, 100));
```

{{< /tab >}}
{{< tab "Go" >}}

```go
sub := image.Sub(firefly.P(10, 10), firefly.S(10, 10))
firefly.DrawSubImage(sub, firefly.P(120, 100))
```

{{< /tab >}}
{{< tab "Zig" >}}

```zig
const sub = image.sub(.{10, 10}, .{10, 10});
ff.drawSubImage(sub, .{120, 100});
```

{{< /tab >}}
{{< tab "TS" >}}

```ts
const sub = image.sub(Point.new(10, 10), Size.new(10, 10));
ff.drawSubImage(sub, Point.new(120, 100));
```

{{< /tab >}}
{{< tab "C/C++" >}}

```c
Point p1 = {10, 10};
Size s1 = {10, 10};
SubImage sub = image.sub(p1, s1);
Point p2 = {120, 100};
draw_sub_image(sub, p2);
```

{{< /tab >}}
{{< tab "Odin" >}}

```odin
sub := firefly.sub(image, firefly.p(10, 10), firefly.s(10, 10))
firefly.draw_sub_image(sub, firefly.p(120, 100))
```

{{< /tab >}}
{{< tab "MoonBit" >}}

```moonbit
let sub = image.sub(Point::new(10, 10), Size::new(10, 10));
@firefly.draw_sub_image(sub, Point::new(120, 100));
```

{{< /tab >}}
{{< tab "Lua" >}}

```lua
-- TODO
```

{{< /tab >}}
{{< /tabs >}}

If the image uses a custom color palette, you can add the palette into the `palettes` table in `firefly.toml` and reference it in the `file`:

```toml
# https://lospec.com/palette-list/pico-8
[palettes.pico-8]
1 = 0x000000
2 = 0x1D2B53
3 = 0x7E2553
# ...

[files]
img = { path = "image.png", palette = "pico-8" }
```

Just like for the runtime palette definitions, `firefly.toml` snippets for some color palettes are available at [palettes.fireflyzero.com](https://palettes.fireflyzero.com/).

## 🔤 Text

First, go to [fonts.fireflyzero.com](https://fonts.fireflyzero.com/) and download the font that you'd like to use. Then add it into `firefly.toml` as you add images:

```toml
[files]
font = { path = "eg_6x9.fff" }
```

Now you can load the font from ROM as you load images and call `draw_text` with the text you want to render and the font.

{{< tabs >}}
{{< tab "Rust" >}}

```rust
draw_text("Welcome, adventurer!", &font, Point::new(60, 10));
```

{{< /tab >}}
{{< tab "Go" >}}

```go
firefly.DrawText("Welcome, adventurer!", font, firefly.P(60, 10))
```

{{< /tab >}}
{{< tab "Zig" >}}

```zig
ff.drawText("Welcome, adventurer!", font, .{ .x = 60, .y = 10 });
```

{{< /tab >}}
{{< tab "TS" >}}

```ts
ff.drawText("Welcome, adventurer!", font, ff.Point.new(60, 10));
```

{{< /tab >}}
{{< tab "C" >}}

```c
Point p = {60, 10};
draw_text("Welcome, adventurer!", font, p);
```

{{< /tab >}}
{{< tab "C++" >}}

```c++
draw_text("Welcome, adventurer!", font, {60, 10});
```

{{< /tab >}}
{{< tab "Odin" >}}

```odin
firefly.draw_text("Welcome, adventurer!", font, firefly.p(60, 10))
```

{{< /tab >}}
{{< tab "MoonBit" >}}

```moonbit
@firefly.draw_text("Welcome, adventurer!", font, Point::new(60, 10));
```

{{< /tab >}}
{{< tab "Lua" >}}

```lua
firefly.draw_text("Welcome, adventurer!", font, {x=60, y=10})
```

{{< /tab >}}
{{< /tabs >}}

{{< hint info >}}
The text does not automatically wrap. If you need word wrapping, you should add new lines into the text yourself.
{{< /hint >}}

If you want to include in your app a link, you can use `draw_qr` to render a QR code.

## 🖌 Canvas

To create a new image, you need to pass the image size and a color. The color will be used to represent transparency. For example, if the transparency color is Red, then the image cannot contain the red color. So when you draw a red circle on the image, it will be represented as a transparent "hole" in the image instead.

{{< tabs >}}
{{< tab "Rust" >}}

```rust
let image = ImageBuf::new(Size::new(120, 120), Color::Black);
```

{{< /tab >}}
{{< tab "Go" >}}

```go
image := firefly.NewImage(firefly.Size{W: 120, H: 120}, firefly.ColorBlack)
```

{{< /tab >}}
{{< tab "Zig" >}}

```zig
// TODO: Canvas not fully supported by Zig yet.
```

{{< /tab >}}
{{< tab "TS" >}}

```ts
const image = ff.Canvas.new(ff.Size.new(120, 120), ff.Color.Black);
```

{{< /tab >}}
{{< tab "C/C++" >}}

```c
// TODO: Canvas not supported by C yet.
```

{{< /tab >}}
{{< tab "Odin" >}}

```odin
image := firefly.empty_image(firefly.s(120, 120), firefly.Color.Black)
```

{{< /tab >}}
{{< tab "MoonBit" >}}

```moonbit
let image = Image::new(Size::new(120, 120), Black)
```

{{< /tab >}}
{{< tab "Lua" >}}

```lua
-- TODO: Canvas not supported by Lua yet
```

{{< /tab >}}
{{< /tabs >}}

Any image (both loaded from a file or created from scratch) can be set as a "canvas". When a canvas is set (using `set_canvas`), almost all subsequent drawing operations will target that image instead of the screen. To make the functions target the screen again, call `unset_canvas`.

Canvas is useful for image manipulation and for drawing from scratch some complex images that should be persisted between multiple frames. For example, it can store dirt on a character, bullet marks on walls, debris on the ground, randomly generated terrain, etc.

{{< tabs >}}
{{< tab "Rust" >}}

```rust
set_canvas(&image);
// fill canvas with white color
clear_screen(Color::White);
unset_canvas();
```

{{< /tab >}}
{{< tab "Go" >}}

```go
firefly.SetCanvas(image)
// fill canvas with white color
firefly.ClearScreen(firefly.ColorWhite)
firefly.UnsetCanvas()
```

{{< /tab >}}
{{< tab "Zig" >}}

```zig
ff.setCanvas(image);
ff.clearScreen(.white);
ff.unsetCanvas();
```

{{< /tab >}}
{{< tab "TS" >}}

```ts
ff.setCanvas(image);
// fill canvas with white color
ff.clearScreen(ff.Color.White);
ff.unsetCanvas();
```

{{< /tab >}}
{{< tab "C/C++" >}}

```c
// TODO: Canvas not supported by C yet.
```

{{< /tab >}}
{{< tab "Odin" >}}

```odin
firefly.set_canvas(image)
// fill canvas with white color
firefly.clear_screen(firefly.Color.White)
firefly.unset_canvas()
```

{{< /tab >}}
{{< tab "MoonBit" >}}

```moonbit
@firefly.set_canvas(image)
// fill canvas with white color
@firefly.clear_screen(White)
@firefly.unset_canvas()
```

{{< /tab >}}
{{< tab "Lua" >}}

```lua
-- TODO: Canvas not supported by Lua yet
```

{{< /tab >}}
{{< /tabs >}}

Some of the functions most commonly used with canvas:

* `flip_x`: flip the image horizontally.
* `flip_y`: flip the image vertically.
* `flip_x` + `flip_y`: rotate the image 180 degrees.
* `clear_screen`: fill the image with a color.
* `draw_point` (and other `draw_` functions): draw on the image.

{{< hint warning >}}
Currently, `draw_text`, `draw_image`, and `draw_sub_image` don't support canvas but it might change in the future. Don't call these functions when you have a canvas set!
{{< /hint >}}

## 🪟 Tiling

### 🧱 Creating levels

Most of the retro games use "sprites": A collection of small square images (usually 8x8 or 16x16 pixels) which are used to tile the screen as a square grid to form the game level.

{{% details "Tiled level example" %}}
![tiling example](/tiling.png)
{{% /details %}}

Sprites are typically all packed on a single image called "spritesheet" (or "atlas").

{{% details "Spritesheet example" %}}
![atlas example](/atlas.png)
{{% /details %}}

To create such levels, you can download an existing spritesheet (for example, from [itch.io](https://itch.io/game-assets/tag-pixel-art)), pick the sprites that you want to use in any image editor (I use [Pinta](https://www.pinta-project.com/releases/)), and arrange them using a level editor (like [Tiled](https://thorbjorn.itch.io/tiled) or [LDtk](https://github.com/deepnight/ldtk)). You can then load the exported level directly as JSON but I prefer to convert it first to bytes (where eah byte is the sprite ID) using a simple Python script which significantly reduces the game size.

{{% details "Python script" %}}

```python
import xml.etree.ElementTree as xml
from pathlib import Path

assets_dir = Path(__file__).parent / 'assets'
tree = xml.parse(assets_dir / 'level.tmx')
root = tree.getroot()
data = root.findall('layer')[0].findall('data')[0]
raw = [int(byte.strip()) for byte in data.text.split(',')]
(assets_dir / 'level.bin').write_bytes(bytes(raw))
```

{{% /details %}}

In Firefly, you can load a spritesheet as an `Image` and then select and render individual sprites as `SubImage` as covered in the [Images](#-images) section.

### 9️⃣ Nine-slice

The [9-slice scaling](https://en.wikipedia.org/wiki/9-slice_scaling) in graphics is a cool technique for rendering pretty boxes. In it, you take a rectangle image and split it into 9 segments:

![9-slice example input](/9slice1.svg)

Then to fill an area with this image you place the corners unchanged and repeat all segments in between:

![9-slice example output](/9slice2.svg)

To draw a 9-slice in Firefly, you load the box as an `Image`, select the middle segment (the green 5 in the example above) as a `SubImage`, and pass it into `draw_nine_slice`:

{{< tabs >}}
{{< tab "Rust" >}}

```rust
let sub = image.sub(Point::new(10, 10), Size::new(10, 10));
draw_nine_slice(sub, Point::new(120, 100), Size::new(50, 40));
```

{{< /tab >}}
{{< tab "Go" >}}

```go
sub := image.Sub(firefly.P(10, 10), firefly.S(10, 10))
firefly.DrawNineSlice(sub, firefly.P(120, 100), firefly.S(50, 40))
```

{{< /tab >}}
{{< tab "Zig" >}}

```zig
const sub = image.sub(.{10, 10}, .{10, 10});
ff.drawNineSlice(sub, .{120, 100}, .{50, 40});
```

{{< /tab >}}
{{< tab "TS" >}}

```ts
const sub = image.sub(Point.new(10, 10), Size.new(10, 10));
ff.drawNineSlice(sub, Point.new(120, 100), Size.new(50, 40));
```

{{< /tab >}}
{{< tab "C/C++" >}}

```c
Point p1 = {10, 10};
Size s1 = {10, 10};
SubImage sub = image.sub(p1, s1);
Point p2 = {120, 100};
Size s2 = {50, 40};
draw_nine_slice(sub, p2, s2);
```

{{< /tab >}}
{{< tab "Odin" >}}

```odin
sub := firefly.sub(image, firefly.p(10, 10), firefly.s(10, 10))
firefly.draw_nine_slice(sub, firefly.p(120, 100), firefly.s(50, 40))
```

{{< /tab >}}
{{< tab "MoonBit" >}}

```moonbit
let sub = image.sub(Point::new(10, 10), Size::new(10, 10));
@firefly.draw_nine_slice(sub, Point::new(120, 100), Size::new(50, 40));
```

{{< /tab >}}
{{< tab "Lua" >}}

```lua
-- TODO
```

{{< /tab >}}
{{< /tabs >}}

## 🔗 Additional resources

If you're looking for 2D pixel sprites for your game, check out:

* [2D assets by Kenney](https://www.kenney.nl/assets/category:2D). Our favorite is [1-Bit Pack](https://www.kenney.nl/assets/1-bit-pack).
* [Pixel Art assets on itch.io](https://itch.io/game-assets/tag-pixel-art). Use tags `8x8` and `16x16` to filter by the desired sprite size (16x16 is prettier but occupies more space on the screen).
* [OpenGameArt.org](https://opengameart.org/art-search-advanced?keys=&field_art_type_tid%5B%5D=9&sort_by=count&sort_order=DESC).

Some assets might have too many colors or a color palette that you don't like. Use [Palette Quantizer](https://lospec.com/palette-quantizer/) to map any assets to any color palette.

Some of our official resources designed specifically for Firefly Zero:

* Catalog of games and tools to get inspired: [catalog.fireflyzero.com](https://catalog.fireflyzero.com/)
* Fonts: [fonts.fireflyzero.com](https://fonts.fireflyzero.com/)
* Color palettes: [palettes.fireflyzero.com](https://palettes.fireflyzero.com/)
* Pixel editor: [pixel.fireflyzero.com](https://pixel.fireflyzero.com/)

Our Pixel Editor is designed to be as simple as possible. If you're looking for a more powerful editor, check out the following:

* [Aseprite](https://www.aseprite.org/)
* [Pixelorama](https://pixelorama.org/)
* [PixiEditor](https://pixieditor.net/)

Lastly, a few more helpful tools:

* [Level editor](https://thorbjorn.itch.io/tiled)
* [Creature generator](https://0x72.itch.io/pixeldudesmaker)
* [Creature editor](https://kenney.itch.io/creature-mixer)
* [Avatar editor](https://kenney.itch.io/avatar-mixer)
* [Spaceship/plane editor](https://kenney.itch.io/ship-mixer)
