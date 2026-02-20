---
title: File formats
type: docs
weight: 3
params:
  icon: fa-solid fa-file
  emoji: 📄
---

## 💾 ROM

Running `firefly_cli export` creates a single-file distribution for an app's ROM. This ROM can be imported back using `firefly_cli import`.

This file is a regular [zip archive](https://en.wikipedia.org/wiki/ZIP_(file_format)) with [zstd](https://en.wikipedia.org/wiki/Zstd) compression. Because zstd compression support is added into the zip specification only in 2020, your archive viewer program might not be able to open it.

## 🏷️ Metadata

The app metadata is stored in `_meta` and encoded using [Postcard Wire Format](https://postcard.jamesmunns.com/wire-format). The schema is defined in [firefly-types](https://github.com/firefly-zero/firefly-types/blob/main/src/meta.rs).

## 🤏 Short Metadata

...

## Media files

For media files, the first byte of the file indicates what type it is:

* `0x11`: mono font v1.
* `0x21`: image v1 (deprecated).
* `0x22`: image v2.
* `0x31`: audio v1.
* `0x41`: screenshot v1.

Firefly uses little endian for everything, including custom file formats.

### 🔤 Mono font

...

### 🖼️ Image

Images can be:

1. Produced by `firefly_cli build` from PNG and bundled into the app ROM.
1. Generated in runtime as `Canvas`.
1. Loaded in runtime by `load_file`.
1. Modified in runtime by `Image` methods.

Image format:

* `0x00`: Magic number (`0x22`).
* `0x01` to `0x02`: Image width (little-endian).
* `0x03`: Transparency color (`0xff` if no transparency).
* `0x04` to the end: Pixel array (4 bits per pixel).

A splash screen (240x160 image) takes 19204 bytes (~18.8 Kb).

### 📸 Screenshot

The screenshot format is used for storing app screenshots in the `data/AUTHOR_ID/APP_ID/shots` directory. The file names are `0001.ffs`, `0002.ffs`, etc. File content:

* `0x00`: magic number (`0x41`).
* `0x01` to `0x30`: color palette. 16 colors in total, each color is stored as 3 bytes RGB.
* `0x31` to `0x4b61`: 160 rows, 120 bytes each. Every byte stores 2 pixels. One pixel is 4 bits representing the color offset in the color palette.

One screenshot is ~19 Kb. 10k screenshots would take 184 Mb of storage.

### 🔊 Audio

...
