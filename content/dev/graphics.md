---
title: 🎨 Graphics
weight: 10
---

## Pixels

The screen size 320x160 pixels, just like GameBoy Advance. Pixels are quite big, so it's safe to draw one pixel wide lines and letters, they will be visible.

Coordinates: x=0 is left, x=320 is right, y=0 is top, and y=160 is bottom.

## Frames

> All those moments will be lost in time.

Each update of the image on the screen is called "frame". Before each frame is rendered, the `render` callback function is called. This is where you should call all drawing functions you need.

Don't draw from the `update` callback: while `update` is called 30.30 times per second (will be soon changed to 60), `render` might be called less often if there are not enough resources. So, if you draw from `update`, you'll waste resources on updating a frame that will be never rendered on the screen.

The frame that you had at the previous update is not cleared. So, if only a small region on the screen needs to be changed, you can redraw only that region and leave the rest intact. If it's not what you want and you'd prefer to redraw the whole frame each time, call `clear_screen`, and it will fill the whole frame with the color you specified.

## Colors

> The enemy of art is the absence of limitations.

Each frame is stored in memory as one of 4 shades of grey. When the time comes to draw the frame on the screen, each of these shades is mapped to one of 4 colors in the color palette.

The default color palette is [kirokaze gameboy](https://lospec.com/palette-list/kirokaze-gameboy):

1. <span style="background-color: #332C50; min-width: 40px; height: 1em; display: inline-block"></span> #332C50
1. <span style="background-color: #46878F; min-width: 40px; height: 1em; display: inline-block"></span> #46878F
1. <span style="background-color: #94E344; min-width: 40px; height: 1em; display: inline-block"></span> #94E344
1. <span style="background-color: #E2F3E4; min-width: 40px; height: 1em; display: inline-block"></span> #E2F3E4

You can modify colors in the palette by calling `set_color` or `set_colors` function (depending on if you want to change one or all of the colors).

You can set any colors you want in any combination you want. However, the best practice is to set colors in the order from darkest to the lightest. The first color is usually almost black, the last is almost white, and the second and the third colors are "colorful" ones for when you need to put an accent on something. Hence for convenience each of the colors in palette has a name:

`DARK`, `ACCENT`, `SECONDARY`, and `LIGHT`

{{< tabs "colors" >}}
{{< tab "Rust" >}}

```rust
firefly::Color::DARK;
firefly::Color::ACCENT;
firefly::Color::SECONDARY;
firefly::Color::LIGHT;
```

{{< /tab >}}
{{< tab "Go" >}}

```go
firefly.ColorDark
firefly.ColorAccent
firefly.ColorSecondary
firefly.ColorLight
```

{{< /tab >}}
{{< /tabs >}}

Looking for inspiration? Check out [lospec.com](https://lospec.com/palette-list/) for nice-looking color palettes.

## More colors

It is possible to render more than 4 colors on a single frame. First, you need to divide the elements on the screen to horizontal regions:

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

1. `draw_point(Point, Size, Color)`
1. `draw_line(Point, Size, LineStyle)`
1. `draw_rect(Point, Size, Style)`
1. `draw_rounded_rect(Point, Size, Size, Style)`
1. `draw_circle(Point, Diameter, Style)`
1. `draw_ellipse(Point, Size, Style)`
1. `draw_triangle(Point, Point, Point, Style)`
1. `draw_arc(Point, Diameter, Angle, Angle, Style)`
1. `draw_sector(Point, Diameter, Angle, Angle, Style)`

## Images

Draw the image you want to render and save it in the project as a grayscale PNG image with up to 4 colors. Then link the image in `firefly.toml`:

```toml
[files]
img = { path = "image.png" }
```

Where `img` is the name of the image in the ROM.

Next, load the image from ROM into the memory:

{{< tabs "load-image" >}}
{{< tab "Rust" >}}

```rust
let file = firefly::rom::load_buf("img");
```

{{< /tab >}}
{{< tab "Go" >}}

```go
// TODO
```

{{< /tab >}}
{{< /tabs >}}

Lastly, call `draw_image` with the image you loaded earlier. The function also accepts `ImageColors` argument which specifies the color to use for each color in the image. The most common use for it is to set one color to zero (`None`) to make background transparent.

## Text

First, go to [fonts.fireflyzero.com](https://fonts.fireflyzero.com/) and download the font that you'd like to use. Then add it into `firefly.toml` as you add images:

```toml
[files]
img = { path = "eg_6x9.fff" }
```

Now you can load the font from ROM as you load images and call `draw_text` with the text you want to render and the font.

The text does not automatically wrap. If you need word wrapping, you should add new lines into the text yourself.
