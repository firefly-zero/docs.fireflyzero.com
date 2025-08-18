---
title: File formats
weight: 10
params:
  icon: fa-solid fa-file
  emoji: 📄
---

For media files, the first byte of the file indicates what type it is:

* `0x11`: mono font v1.
* `0x21`: image v1.
* `0x31`: audio v1.
* `0x41`: screenshot v1.

Firefly uses little endian for everything, including custom file formats.

## ROM

Running `firefly_cli export` creates a single-file distribution for an app's ROM. This ROM can be imported back using `firefly_cli import`.

This file is a regular [zip archive](https://en.wikipedia.org/wiki/ZIP_(file_format)) with [zstd](https://en.wikipedia.org/wiki/Zstd) compression. Because zstd compression support is added into the zip specification only in 2020, your archive program won't be able to open it.

## Image

...

## Screenshot

The screnshot format is used for storing app screenshots in the `data/AUTHOR_ID/APP_ID/shots` directory. The file names are `0001.ffs`, `0002.ffs`, etc. File content:

* `0x00`: magic number (`0x41`).
* `0x01` to `0x30`: color palette. 16 colors in total, each color is stored as 3 bytes RGB.
* `0x31` to `0x4b61`: 160 rows, 120 bytes each. Every byte stores 2 pixels. One pixel is 4 bits representing the color offset in the color palette.

One screenshot is 19 Kb. 10k screenshots would take 184 Mb of storage.

## Audio

...

## Font

...

## Metadata

...

## Short metadata

...
