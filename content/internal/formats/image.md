---
title: Image
weight: 10
params:
  icon: fa-solid fa-file-image
  emoji: 🖼️
---

Images can be:

1. Produced by `firefly_cli build` from PNG and bundled into the app ROM.
1. Generated in runtime as `Canvas`.
1. Loaded in runtime by `load_file`.
1. Modified in runtime by `Image` methods.

## Image format

The image format defines a BPP (Bits Per Pixel) density of either:

- 1 BPP: supports up to 2 colors
- 2 BPP: supports up to 4 colors
- 4 BPP: supports up to 16 colors

Data structure of an image:

| Section | Length (bytes)             | Data
| ------- | -------------------------- | ----
| header  | 1                          | magic number `0x21` (marker that signals that this binary is an image)
| header  | 1                          | BPP (Bits Per Pixel). Either set to `0x01`, `0x02`, or `0x04`
| header  | 2                          | image width (16-bit, little-endian)
| header  | 1                          | transparency color. Only lower 4 bits are used
| header  | `BPP * 2`                  | palette swaps, with 1 nibble (4 bits) per color
| body    | `width * height * BPP / 8` | image body (rest of the image)

The first `5 + BPP * 2` bytes together are considered the header.

## Palette swaps

Palette swaps map pixels in the image to a color in the [color palette]({{< ref "/dev/graphics/" >}}#-colors). The swaps are stored as 4 bits (a nibble) each and go from 0 to 15 (instead of from 1 to 16 in SDKs).

- With 1 BPP, palette is 1 byte and stores 2 colors.
- With 2 BPP, palette is 2 bytes and stores 4 colors.
- With 4 BPP, palette is 8 bytes and stores 16 colors.

Therefore, the representation of a palette swap for a 2-BPP image in the default palette mapping 0 to `Gray` (15-1=0xE), 1 to `Green` (7-1=0x6), 2 to `Blue` (10-1=0x9), and 3 to `Yellow` (5-1=0x4) would be represented as `0xE694`.

## Transparency

Image transparency is decided by the transparency color. Any pixel in the image body that matches the same color as the transparency color are considered transparent.

If the transparency color is set to a value greater than or equal to `1 << BPP`, then the image is considered to have no transparency. Meaning:

- With 1 BPP, if transparency color is `0x02` or higher, then no transparency
- With 2 BPP, if transparency color is `0x04` or higher, then no transparency
- With 4 BPP, if transparency color is `0x10` or higher, then no transparency

For images without transparency it is common to use a value of `0xFF`, though any value above the threshold is equally valid.

## Image body

The image body is a string of pixels whose value references a color in the palette swaps.

- With 1 BPP, each 1-bit pixel targets palette color at index `0x0 - 0x1`
- With 2 BPP, each 2-bit pixel targets palette color at index `0x0 - 0x3`
- With 4 BPP, each 4-bit pixel targets palette color at index `0x0 - 0xF`

Therefore, a 2x2 pixel image with 2-BPP that uses all 4 colors from the palette could be represented by:

```text
hex         0x1b
binary  00011011
```

Using the 2-BPP palette swaps example from above, then the image would look like this in the default palette:

<div class="image-demo"><svg
  xmlns="http://www.w3.org/2000/svg" version="1.1"
  xmlns:xlink="http://www.w3.org/1999/xlink"
  viewBox="0 0 400 400">
  <rect width="200" height="200" x="0" y="0" fill="#556C86"></rect>
  <rect width="200" height="200" x="200" y="0" fill="#38B764"></rect>
  <rect width="200" height="200" x="0" y="200" fill="#3B5DC9"></rect>
  <rect width="200" height="200" x="200" y="200" fill="#FFCD75"></rect>
</svg></div>

## Examples

### Example: 1-BPP

4x4 pixels image with 1-BPP:

- header: 7 bytes
- body: 2 bytes
- total: 9 bytes

```text
     ┌► header
0x21 ┤ ─► magic number (marker that signals that this is an image)
0x01 ┤ ─► bits per pixel (BPP, either 0x01, 0x02, or 0x04)
0x04 ┤ ┬► image width, 16 bit little-endian
0x00 ┤ ┘
0xFF ┤ ─► transparency color
0x42 ┘ ─► 1 byte color palette (2 colors)
     ┌► image body
0xC3 ┤ ─► row 1 & row 2
0x9B ┘ ─► row 3 & row 4
```

<div class="image-demo"><svg
  xmlns="http://www.w3.org/2000/svg" version="1.1"
  xmlns:xlink="http://www.w3.org/1999/xlink"
  viewBox="0 0 400 400">
  <rect width="100" height="100" x="0"   y="0"   fill="#B13E53"></rect>
  <rect width="100" height="100" x="100" y="0"   fill="#B13E53"></rect>
  <rect width="100" height="100" x="200" y="0"   fill="#FFCD75"></rect>
  <rect width="100" height="100" x="300" y="0"   fill="#FFCD75"></rect>
  <rect width="100" height="100" x="0"   y="100" fill="#FFCD75"></rect>
  <rect width="100" height="100" x="100" y="100" fill="#FFCD75"></rect>
  <rect width="100" height="100" x="200" y="100" fill="#B13E53"></rect>
  <rect width="100" height="100" x="300" y="100" fill="#B13E53"></rect>
  <rect width="100" height="100" x="0"   y="200" fill="#B13E53"></rect>
  <rect width="100" height="100" x="100" y="200" fill="#FFCD75"></rect>
  <rect width="100" height="100" x="200" y="200" fill="#FFCD75"></rect>
  <rect width="100" height="100" x="300" y="200" fill="#B13E53"></rect>
  <rect width="100" height="100" x="0"   y="300" fill="#B13E53"></rect>
  <rect width="100" height="100" x="100" y="300" fill="#FFCD75"></rect>
  <rect width="100" height="100" x="200" y="300" fill="#B13E53"></rect>
  <rect width="100" height="100" x="300" y="300" fill="#B13E53"></rect>
</svg></div>

### Example: 2-BPP

4x4 pixels image with 2-BPP:

- header: 9 bytes
- body: 4 bytes
- total: 13 bytes

```text
     ┌► header
0x21 ┤ ─► magic number (marker that signals that this is an image)
0x02 ┤ ─► bits per pixel (BPP, either 0x01, 0x02, or 0x04)
0x04 ┤ ┬► image width, 16 bit little-endian
0x00 ┤ ┘
0xFF ┤ ─► transparency color
0x2B ┤ ┬► 2 bytes color palette (4 colors)
0x5A ┘ ┘
     ┌► image body
0xEC ┤ ─► row 1
0xAF ┤ ─► row 2
0x50 ┤ ─► row 3
0x91 ┘ ─► row 4
```

<div class="image-demo"><svg
  xmlns="http://www.w3.org/2000/svg" version="1.1"
  xmlns:xlink="http://www.w3.org/1999/xlink"
  viewBox="0 0 400 400">
  <rect width="100" height="100" x="0"   y="0"   fill="#41A6F6"></rect>
  <rect width="100" height="100" x="100" y="0"   fill="#A7F070"></rect>
  <rect width="100" height="100" x="200" y="0"   fill="#41A6F6"></rect>
  <rect width="100" height="100" x="300" y="0"   fill="#B13E53"></rect>
  <rect width="100" height="100" x="0"   y="100" fill="#A7F070"></rect>
  <rect width="100" height="100" x="100" y="100" fill="#A7F070"></rect>
  <rect width="100" height="100" x="200" y="100" fill="#41A6F6"></rect>
  <rect width="100" height="100" x="300" y="100" fill="#41A6F6"></rect>
  <rect width="100" height="100" x="0"   y="200" fill="#73EFF7"></rect>
  <rect width="100" height="100" x="100" y="200" fill="#73EFF7"></rect>
  <rect width="100" height="100" x="200" y="200" fill="#B13E53"></rect>
  <rect width="100" height="100" x="300" y="200" fill="#B13E53"></rect>
  <rect width="100" height="100" x="0"   y="300" fill="#A7F070"></rect>
  <rect width="100" height="100" x="100" y="300" fill="#73EFF7"></rect>
  <rect width="100" height="100" x="200" y="300" fill="#B13E53"></rect>
  <rect width="100" height="100" x="300" y="300" fill="#73EFF7"></rect>
</svg></div>

### Example: 4-BPP

4x4 pixels image with 4-BPP:

- header: 13 bytes
- body: 8 bytes
- total: 21 bytes

```text
     ┌► header
0x21 ┤ ─► magic number (marker that signals that this is an image)
0x04 ┤ ─► bits per pixel (BPP, either 0x01, 0x02, or 0x04)
0x04 ┤ ┬► image width, 16 bit little-endian
0x00 ┤ ┘
0x01 ┤ ─► transparency color
0x01 ┤ ┬► 8 bytes color palette (16 colors)
0x23 ┤ ┤
0x45 ┤ ┤
0x67 ┤ ┤
0x89 ┤ ┤
0xAB ┤ ┤
0xCD ┤ ┤
0xEF ┘ ┘
          ┌► image body
0x01 0x23 ┤ ─► row 1
0x45 0x67 ┤ ─► row 2
0x89 0xAB ┤ ─► row 3
0xCD 0xEF ┘ ─► row 4
```

<div class="image-demo"><svg
  xmlns="http://www.w3.org/2000/svg" version="1.1"
  xmlns:xlink="http://www.w3.org/1999/xlink"
  viewBox="0 0 400 400">
  <rect width="100" height="100" x="0"   y="0"   fill="#1A1C2C"></rect>
  <rect width="100" height="100" x="100" y="0"   fill="#5D275D"></rect>
  <rect width="100" height="100" x="200" y="0"   fill="#B13E53"></rect>
  <rect width="100" height="100" x="300" y="0"   fill="#EF7D57"></rect>
  <rect width="100" height="100" x="0"   y="100" fill="#FFCD75"></rect>
  <rect width="100" height="100" x="100" y="100" fill="#A7F070"></rect>
  <rect width="100" height="100" x="200" y="100" fill="#38B764"></rect>
  <rect width="100" height="100" x="300" y="100" fill="#257179"></rect>
  <rect width="100" height="100" x="0"   y="200" fill="#29366F"></rect>
  <rect width="100" height="100" x="100" y="200" fill="#3B5DC9"></rect>
  <rect width="100" height="100" x="200" y="200" fill="#41A6F6"></rect>
  <rect width="100" height="100" x="300" y="200" fill="#73EFF7"></rect>
  <rect width="100" height="100" x="0"   y="300" fill="#F4F4F4"></rect>
  <rect width="100" height="100" x="100" y="300" fill="#94B0C2"></rect>
  <rect width="100" height="100" x="200" y="300" fill="#566C86"></rect>
  <rect width="100" height="100" x="300" y="300" fill="#333C57"></rect>
</svg></div>
