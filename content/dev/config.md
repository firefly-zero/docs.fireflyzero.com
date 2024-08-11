---
title: ⚙️ firefly.toml
weight: 6
---

## ⚙️ firefly.toml

The `firefly.toml` configuration file tells firefly-cli how to build a ROM for the project. It should be placed at the root of the project (though you can explicitly specify the path using `--config`) and must be in the [TOML](https://toml.io/en/) format.

Required:

* `author_id` (string): your username. It should be unique, otherwise users may get a warning about invalid signature when launching your app. The best way to ensure that your author_id is unique is to add it into [catalog.fireflyzero.com](https://catalog.fireflyzero.com/). There are also limitations on the length of the ID and used characters. If your ID (or any of the options below) is invalid, the `build` command will tell you.
* `app_id` (string): the app ID. Must be unique for the given author. THe combination `author_id.app_id` is the full ID of the app, and that must be globally unique.
* `author_name` (string): your name. It will be shown in the launcher next to the app name. It must use the latin alphabet. Non-latin names have to be transliterated.
* `app_name` (string): the human-readable name of the game. Shown in the launcher.

Optional:

* `lang` (string): the programming language of the app source code. Dictates the build command that is used to build the WebAssembly binary.
* `compile_args` (array of strings): an array of additional CLI arguments to pass into the command used to build the WebAssembly binary. The command is language-specific: it will be `cargo` for Rust, `tinygo` for Go, `zig` for Zig, etc.
* `launcher` (boolean): set to `true` if the app is a launcher. The launcher is the first app that starts when the device (or emulator) is launched. Its job is to provide means for launching all other apps on the device.
* `sudo` (boolean): set to `true` if the app needs access to privilieged functions, like reading files in other apps or starting other apps.
* `cheats` (table): specifies how a cheat code should be converted to a number. For example, `set-health = 3` means that when you call `firefly_cli cheat set-health 100`, the `cheat` callback in the running app will be called with values `3` and `100`.
* `files` (table): covered below.

## files

The `[files]` optional table lists additional files (like game assets) that you want to include into the ROM.

The key (the text on the left from `=`) is how the file will be called in the ROM. This is how you referrer to the file when loading it from your code. It must be short and unique within the app. It also shouldn't have an extension.

The value is an inline table that may have the following keys:

* `path` (string, required): the path to the asset to include.
* `url` (string): the URL from which to download the file if it doesn't exist in `path`.
* `sha256` (string): the [SHA-256](https://en.wikipedia.org/wiki/SHA-2) hash of the file. Validated only when downloading the file from the `url`. If the specified hash doesn't match the actual one, the `build` command will fail. It's not required but recommended to always include it if you specify `url`.
* `copy` (bool): set to `true` to copy the file as-is without any modifications. If not specified, the `build` command will try to convert the file into a native format. For example, PNG images will be converted into the native Firefly image format.

{{< button relref="./callbacks.md" >}}➡️ Callbacks{{< /button >}}
