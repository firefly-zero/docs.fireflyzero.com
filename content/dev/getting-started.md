---
title: Getting started
weight: 5
params:
  art: /hello.png
  icon: fa-solid fa-play
  emoji: ▶️
---

## 👉 Pick the language

Firefly Zero supports lots of programming languages:

* 🦀 Rust
* 🏃 Go
* 🐀 C and C++
* ⚡️ Zig
* 🐰 MoonBit
* 🟦 AssemblyScript (a subset of TypeScript)

Experimental:

* 🌙 Lua
* 🧪 Elixir
* ⌛ Coming soon: more languages (Python, JS, Kotlin).

For simple apps and games, it's a good idea to stick to what you already know. But if you're ready to learn something new for better results, we recommend using Go. It's easy to learn, sufficiently fast, and memory-safe.

For simple adventure games, it's also possible to use [Bulb]({{< ref "/dev/bulb/" >}}) or [Bitsy](https://bitsy.org/).

## 📥 Install tools

1. [Install firefly-cli and firefly-emulator]({{< ref "/user/installation/" >}})
1. Install [WebAssembly](https://webassembly.org/) compiler for your language:

{{< tabs >}}
{{< tab "Rust" >}}

```bash
rustup update nightly
rustup component add rust-src --toolchain nightly
rustup target add wasm32-unknown-unknown
```

{{< /tab >}}
{{< tab "Go" >}}

1. [Install Go](https://go.dev/dl/)
1. [Install TinyGo](https://tinygo.org/getting-started/install/)

{{< /tab >}}
{{< tab "Zig" >}}

[Install Zig](https://ziglang.org/download/). Make sure to select the latest stable release, NOT a "master" build.

{{< /tab >}}
{{< tab "TS" >}}

[Install Node.js and npm](https://nodejs.org/en/download/current).

{{< /tab >}}
{{< tab "C/C++" >}}

The preferred way to build a C (or C++) app is using [wasi-sdk](https://github.com/WebAssembly/wasi-sdk):

1. Go to [wasi-sdk releases](https://github.com/WebAssembly/wasi-sdk/releases).
1. Download and install the latest release for your OS.
1. This should install wasi-sdk into `/opt/wasi-sdk`. If you used an alternative installation method and installed wasi-sdk in a different place, provide the absolute path to it in the `WASI_SDK_PATH` environment variable.

{{< /tab >}}
{{< tab "MoonBit" >}}

```bash
curl -fsSL https://cli.moonbitlang.com/install/unix.sh | bash
```

{{< /tab >}}
{{< tab "Lua" >}}

Nothing to install for Lua, you're ready to go!

{{< /tab >}}
{{< tab "Bitsy" >}}

Nothing to install for Bitsy, you're ready to go!

{{< /tab >}}
{{< tab "Bulb" >}}

Nothing to install for Bulb, you're ready to go!

{{< /tab >}}
{{< /tabs >}}

## 💻 Create the project

A new project can be created using `firefly_cli new`:

{{< tabs >}}
{{< tab "Rust" >}}

```bash
firefly_cli new --lang=rust hello-world
```

{{< /tab >}}
{{< tab "Go" >}}

```bash
firefly_cli new --lang=go hello-world
```

{{< /tab >}}
{{< tab "Zig" >}}

```bash
firefly_cli new --lang=zig hello-world
```

{{< /tab >}}
{{< tab "TS" >}}

```bash
firefly_cli new --lang=as hello-world
```

{{< /tab >}}
{{< tab "C" >}}

```bash
firefly_cli new --lang=c hello-world
```

{{< /tab >}}
{{< tab "C++" >}}

```bash
firefly_cli new --lang=cpp hello-world
```

{{< /tab >}}
{{< tab "MoonBit" >}}

```bash
firefly_cli new --lang=moon hello-world
```

{{< /tab >}}
{{< tab "Lua" >}}

```bash
firefly_cli new --lang=lua hello-world
```

{{< /tab >}}
{{< tab "Bitsy" >}}

```bash
firefly_cli new --lang=bitsy hello-world
```

{{< /tab >}}
{{< tab "Bulb" >}}

```bash
firefly_cli new --lang=bulb hello-world
```

{{< /tab >}}
{{< /tabs >}}

In this example, it will create `hello-world` directory and initialize in it a new app called `hello-world` using your chosen programming language. Don't think about it too hard, you can later change the project name in the config (`hello-world/firefly.toml`).

## 🏃 Build and run

1. Build and install the app: `firefly_cli build`
1. Run the last built app: `firefly_emulator`

Have troubles using emulator? Check out the [emulator user guide]({{< ref "/user/emulator/" >}}).

## 📦 Distribute

1. Export an app into a zip file: `firefly_cli export`.
1. Publish the file anywhere you like. For open-source projects, a good option is Github Releases.
1. People then can download and install the app:

    ```bash
    firefly_cli import ./joearms.hello-world.zip
    ```

1. Optional: add your app into the catalog: [catalog.fireflyzero.com](https://catalog.fireflyzero.com/).

## 🧠 Further reading

There are several things you should know to make a game:

1. How the runtime works in general. Start by reading about [firefly.toml]({{< ref "/dev/config/" >}}) and then go through all other pages in this documentation in order.
1. How to make games and what patterns make it easier. We recommend reading [Game Programming Patterns](http://gameprogrammingpatterns.com/contents.html).

And take a look at resources for your language:

{{< tabs >}}
{{< tab "Rust" >}}

* [SDK source code](https://github.com/firefly-zero/firefly-rust)
* [SDK API docs](https://docs.rs/firefly-rust/latest/firefly_rust/)
* [Learn Rust](https://doc.rust-lang.org/stable/book/)

{{< /tab >}}
{{< tab "Go" >}}

* [SDK source code](https://github.com/firefly-zero/firefly-go)
* [SDK API docs](https://pkg.go.dev/github.com/firefly-zero/firefly-go)
* [Learn Go](https://gobyexample.com/)

{{< /tab >}}
{{< tab "Zig" >}}

* [SDK source code](https://github.com/firefly-zero/firefly-zig)
* [Learn Zig](https://zig.guide/)

{{< /tab >}}
{{< tab "TS" >}}

* [SDK source code](https://github.com/firefly-zero/firefly-as)
* [Learn AssemblyScript](https://www.assemblyscript.org/concepts.html)

{{< /tab >}}
{{< tab "C" >}}

* [SDK source code](https://github.com/firefly-zero/firefly-c)
* [Learn C](https://www.w3schools.com/c/c_intro.php)

{{< /tab >}}
{{< tab "C++" >}}

* [SDK source code](https://github.com/firefly-zero/firefly-c)
* [Learn C++](https://www.w3schools.com/cpp/cpp_intro.asp)

{{< /tab >}}
{{< tab "MoonBit" >}}

* [SDK source code](https://github.com/firefly-zero/firefly-moon)
* [SDK API docs](https://mooncakes.io/docs/applejag/firefly)
* [Learn MoonBit](https://docs.moonbitlang.com/en/latest/language/fundamentals.html)

{{< /tab >}}
{{< tab "Lua" >}}

* [SDK source code](https://github.com/firefly-zero/firefly-lua)
* [Learn Lua](https://www.tutorialspoint.com/lua/index.htm)

{{< /tab >}}
{{< tab "Elixir" >}}

* [SDK source code](https://github.com/firefly-zero/firefly-elixir)
* [Elixir WebAssembly compiler](https://github.com/RoyalIcing/Orb)
* [Learn Elixir](https://elixirschool.com/en/lessons/basics/basics)

{{< /tab >}}
{{< tab "Bitsy" >}}

You can edit the `main.bitsy` file using the official Bitsy editor: [make.bitsy.org](https://make.bitsy.org/). Use the "load data" button to upload the file into the editor and "save data" to download the file from the editor back into the saved file.

To learn how to make Bitsy games, go to the [official documentation](https://make.bitsy.org/docs/).

{{< /tab >}}
{{< tab "Bulb" >}}

Go to the [Bulb documentation]({{< ref "/dev/bulb/" >}}) to learn how to write a game.

{{< /tab >}}
{{< /tabs >}}
