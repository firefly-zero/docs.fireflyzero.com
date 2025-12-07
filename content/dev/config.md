---
title: firefly.toml
weight: 6
params:
  art: /toml.png
  icon: fa-solid fa-cog
  emoji: ⚙️
---

The `firefly.toml` configuration file tells firefly-cli how to build a ROM for the project. It should be placed at the root of the project (though you can explicitly specify the path using `--config`) and must be in the [TOML](https://toml.io/en/) format.

Required:

* `author_id` (string): your username. It should be unique, otherwise users may get a warning about invalid signature when launching your app. The best way to ensure that your author_id is unique is to add it into [catalog.fireflyzero.com](https://catalog.fireflyzero.com/). There are also limitations on the length of the ID and used characters. If your ID (or any of the options below) is invalid, the `build` command will tell you.
* `app_id` (string): the app ID. Must be unique for the given author. THe combination `author_id.app_id` is the full ID of the app, and that must be globally unique.
* `author_name` (string): your name. It will be shown in the launcher next to the app name. It must use the latin alphabet. Non-latin names have to be transliterated.
* `app_name` (string): the human-readable name of the game. Shown in the launcher.

Optional:

* `lang` (string): the programming language of the app source code. Dictates the build command that is used to build the WebAssembly binary. If not specified, the language will be automatically detected.
* `compile_args` (array of strings): an array of additional CLI arguments to pass into the command used to build the WebAssembly binary. The command is language-specific: it will be `cargo` for Rust, `tinygo` for Go, `zig` for Zig, etc.
* `launcher` (boolean): set to `true` if the app is a launcher. The launcher is the first app that starts when the device (or emulator) is launched. Its job is to provide means for launching all other apps on the device.
* `sudo` (boolean): set to `true` if the app needs access to privilieged functions, like reading files in other apps or starting other apps.
* `cheats` (table): specifies how a cheat code should be converted to a number. For example, `set-health = 3` means that when you call `firefly_cli runtime cheat set-health 100`, the `cheat` callback in the running app will be called with values `3` and `100`.
* `files` (table): covered below.
* `badges` (table): see [Badges and scores]({{< ref "stats.md#-badges" >}}).
* `boards` (table): see [Badges and scores]({{< ref "stats.md#-boards" >}}).
* `palettes` (table): see [Images]({{< ref "graphics.md#-images" >}}).

## files

The `[files]` optional table lists additional files (like game assets) that you want to include into the ROM.

The key (the text on the left from `=`) is how the file will be called in the ROM. This is how you referrer to the file when loading it from your code. It must be short and unique within the app. It also shouldn't have an extension.

The value is an inline table that may have the following keys:

* `path` (string, required): the path to the asset to include.
* `url` (string): the URL from which to download the file if it doesn't exist in `path`.
* `sha256` (string): the [SHA-256](https://en.wikipedia.org/wiki/SHA-2) hash of the file. Validated only when downloading the file from the `url`. If the specified hash doesn't match the actual one, the `build` command will fail. It's not required but recommended to always include it if you specify `url`.
* `copy` (bool): set to `true` to copy the file as-is without any modifications. If not specified, the `build` command will try to convert the file into a native format. For example, PNG images will be converted into the native Firefly image format.
* `palette` (string): the name of the color palette to use for parsing the image.

There are a few file names that have a special meaning:

* `_bin`: the wasm binary to include instead of trying to build it from source. See the "Customizing builds" section below.
* `_splash`: the splash screen to be rendered before launching the app. In other words, a static loading screen.

## Example

```toml
author_id = "lux"
app_id = "snek"
author_name = "Lux"
app_name = "Snek"

[files]
font = { path = "font.fff", url = "https://fonts.fireflyzero.com/fonts/ascii/eg_4x6.fff", sha256 = "dd90ec6478b7cab75e73abde35e76ef3e7e08a2682be83a5ef859607e41e4e68" }
_splash = { path = "splash.png" }

[cheats]
move-apple = 1 # Move apple into a new random position
inc-score = 2  # Increment the score by the given value
dec-score = 3  # Decrement the score by the given value

[badges]
1 = { name = "m i tasti", descr = "bite yourself" }
2 = { name = "u r tasti", descr = "bite someone else" }
3 = { name = "apel tasti", descr = "eat 100 apples", steps = 100 }
```

## Customizing builds

Does your app require a complicated build process? No problem! There are a few ways to customize the compilation:

1. The `compile_args` option allows you to pass additional CLI arguments in the build command that firefly_cli invokes internally. For most compilers, it will be added at the end of all the default arguments. But for some compilers, like C/C++ (wasi-sdk), it will overwrite some of the defaults.
1. Language-specific configuration files:
    1. **🦀 Rust**: binary builds can be customized using `Cargo.toml` (see [Cargo Targets](https://doc.rust-lang.org/cargo/reference/cargo-targets.html)) and `.cargo/config.toml` (see [Cargo Configuration](https://doc.rust-lang.org/cargo/reference/config.html)).
    1. **🏃 Go**: you can create a `target.json` file in the root of your project. It will fully replace [the default `target.json`](https://github.com/firefly-zero/firefly-cli/blob/main/src/target.json) used by firefly_cli. See [Important Build Options](https://tinygo.org/docs/reference/usage/important-options/).
    1. **⚡️ Zig**: you can create a `build.zig` file in the root of your project. It will fully replace the default `build.zig` used by firefly_cli.
    1. **🐀 C/C++**: clang doesn't have a build configuration file. Use other ways to customize the build.
    1. **🐰 MoonBit**: see [Package Configuration](https://docs.moonbitlang.com/en/latest/toolchain/moon/package.html).
1. Lastly, you can build the wasm binary yourself in whatever way works for you. It is especially useful when developing a new SDK for a not yet supported language. Tell firefly_cli to copy your binary as `_bin` file, and it will skip the compilation step:

    ```toml
    [files]
    _bin = { path = "main.wasm", copy = true }
    ```
