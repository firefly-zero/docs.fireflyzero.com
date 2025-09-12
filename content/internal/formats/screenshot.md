---
title: Screenshot
weight: 10
params:
  icon: fa-solid fa-camera
  emoji: 📸
---

The screenshot format is used for storing app screenshots in the `data/AUTHOR_ID/APP_ID/shots` directory. The file names are `0001.ffs`, `0002.ffs`, etc. File content:

* `0x00`: magic number (`0x41`).
* `0x01` to `0x30`: color palette. 16 colors in total, each color is stored as 3 bytes RGB.
* `0x31` to `0x4b61`: 160 rows, 120 bytes each. Every byte stores 2 pixels. One pixel is 4 bits representing the color offset in the color palette.

One screenshot is 19 Kb. 10k screenshots would take 184 Mb of storage.
