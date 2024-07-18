---
title: 📕 Terms
weight: 60
---

## 📕 Terms

Below are different terms that the documentation uses. If there is a technical word in the ocumentation that you don't understand, it should be in there. If it's not, send us a pull request or open an issue!

* **Asset** is a file that an app needs but which isn't the code. It includes sprites, music, sounds, sometimes dialogs and configurations, etc.
* **Frame** is what is show on the screen at one specific moment. Each frame is a rectangle of 240 per 160 pixels.
* **ROM** is a distribution of your game. It includes a WebAssembly binary, game assets, metadata, signature, etc. A ROM is distributed in a ZIP (`*.zip`) file and on the device is stored as a collection of files in a directory in `/roms/`.
* **TOML** is a configuration format that we use for the `firefly.toml` config. It's stricter than YAML and more readable than JSON. If you've seen INI (`*.ini`) files in WIndows games, TOML should look very familiar.
* **WebAssembly** (aka **wasm**) is a binary format in which all Firefly apps compile. It's like EXE (`*.exe`) on Windows.
