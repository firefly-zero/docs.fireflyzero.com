---
title: 🎨 Graphics
weight: 15
---

## Pixels

The screen size 240x160 pixels, just like GameBoy Advance. Pixels are quite big, so it's safe to draw one pixel wide lines and letters, they will be visible.

Coordinates: x=0 is left, x=240 is right, y=0 is top, and y=160 is bottom.

## Frames

> All those moments will be lost in time.

Each update of the image on the screen is called "frame". Before each frame is rendered, the `render` callback function is called. This is where you should call all drawing functions you need.

Don't draw from the `update` callback: while `update` is called 30.30 times per second (will be soon changed to 60), `render` might be called less often if there are not enough resources. So, if you draw from `update`, you'll waste resources on updating a frame that will be never rendered on the screen.

The frame that you had at the previous update is not cleared. So, if only a small region on the screen needs to be changed, you can redraw only that region and leave the rest intact. If it's not what you want and you'd prefer to redraw the whole frame each time, call `clear_screen`, and it will fill the whole frame with the color you specified.

## Colors

> The enemy of art is the absence of limitations.

Each frame is stored in memory as one of 16 shades of gray. When the time comes to draw the frame on the screen, each of these shades is mapped to one of 16 colors in the color palette.

The default color palette is [Sweetie 16](https://lospec.com/palette-list/sweetie-16):

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

{{< tabs "set-color" >}}
{{< tab "Rust" >}}

```rust
firefly_rust::set_color(
    firefly_rust::Color::Red,
    firefly_rust::RGB{r: 0xff, g: 0x00, b: 0x00},
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
{{< /tabs >}}

Looking for inspiration? Check out [lospec.com](https://lospec.com/palette-list/) for nice-looking color palettes.

## More colors

It is possible to render more than 16 colors on a single frame. First, you need to divide the elements on the screen to horizontal regions:

... (TODO: add an image with an example)

Then you can provide a `render_line` callback function. The callback accepts the line for each it is called and returns the next line before which it should be called again. For example, it is called with 0 first time and if it then returns 100, it will be called again before rendering the line 100. If then it returns 0, it will be called again only when rendering the next frame.

This callback must be as fast as possible and all it should do is change the colors in the palette. In other words, the callback can be used to swap the colors in the palette on the go, as lines are rendered on the screen.

## Shapes

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

{{< tabs "draw-triangle" >}}
{{< tab "Rust" >}}

```rust
ff::draw_triangle(
    ff::Point { x: 60, y: 10 },
    ff::Point { x: 40, y: 40 },
    ff::Point { x: 80, y: 40 },
    ff::Style {
        fill_color:   ff::Color::Accent,
        stroke_color: ff::Color::Secondary,
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
    firefly.Style{FillColor: 2, StrokeColor: 3, StrokeWidth: 1},
)
```

{{< /tab >}}
{{< /tabs >}}

## Images

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

{{< tabs "load-image" >}}
{{< tab "Rust" >}}

```rust
let file = firefly_rust::rom::load_buf("img");
```

{{< /tab >}}
{{< tab "Go" >}}

```go
file := firefly.LoadROMFile("img");
```

{{< /tab >}}
{{< /tabs >}}

Lastly, call `draw_image` with the image you loaded earlier.

## Text

First, go to [fonts.fireflyzero.com](https://fonts.fireflyzero.com/) and download the font that you'd like to use. Then add it into `firefly.toml` as you add images:

```toml
[files]
img = { path = "eg_6x9.fff" }
```

Now you can load the font from ROM as you load images and call `draw_text` with the text you want to render and the font.

The text does not automatically wrap. If you need word wrapping, you should add new lines into the text yourself.
