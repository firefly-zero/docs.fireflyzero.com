---
title: 📄 File formats
weight: 10
---

For media files, the first byte of the file indicates what type it is:

* `0x11`: mono font v1.
* `0x21`: image v1.
* `0x31`: audio v1.

## ROM

Running `firefly_cli export` creates a single-file distribution for an app's ROM. This ROM can be imported back using `firefly_cli import`.

This file is a regular [zip archive](https://en.wikipedia.org/wiki/ZIP_(file_format)) with [zstd](https://en.wikipedia.org/wiki/Zstd) compression. Because zstd compression support is added into the zip specification only in 2020, your archive program won't be able to open it.

## Image

...

## Audio

...

## Font

...

## Metadata

...

## Short metadata

...
