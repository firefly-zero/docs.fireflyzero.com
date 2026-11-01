---
title: Your first app
weight: 6
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
* 🐦‍⬛ Odin
* 🐰 MoonBit
* 🟦 AssemblyScript (a subset of TypeScript)

Experimental:

* 🌙 Lua
* 🧪 Elixir

For simple apps and games, it's a good idea to stick to what you already know. But if you're ready to learn something new for better results, we recommend using Go. It's easy to learn, sufficiently fast, and memory-safe.

For simple adventure games, it's also possible to use [Bulb]({{< ref "/dev/bulb/" >}}) or [Bitsy](https://bitsy.org/).

## 📥 Install tools

1. [Install firefly_cli]({{< ref "/dev/installation/" >}})
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
{{< tab "Odin" >}}

1. Install [odin](https://odin-lang.org/):
    1. Go to [odin releases](https://github.com/odin-lang/Odin/releases)
    1. Download and extract the latest release for your OS.
    1. Add the `bin` directory from the extracted path into `$PATH`.
1. Install [wasi-sdk](https://github.com/WebAssembly/wasi-sdk):
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

A new project can be created using `ff new`:

{{< tabs >}}
{{< tab "Rust" >}}

```bash
ff new --lang=rust hello-world
```

{{< /tab >}}
{{< tab "Go" >}}

```bash
ff new --lang=go hello-world
```

{{< /tab >}}
{{< tab "Zig" >}}

```bash
ff new --lang=zig hello-world
```

{{< /tab >}}
{{< tab "TS" >}}

```bash
ff new --lang=as hello-world
```

{{< /tab >}}
{{< tab "C" >}}

```bash
ff new --lang=c hello-world
```

{{< /tab >}}
{{< tab "C++" >}}

```bash
ff new --lang=cpp hello-world
```

{{< /tab >}}
{{< tab "Odin" >}}

```bash
ff new --lang=odin hello-world
```

{{< /tab >}}
{{< tab "MoonBit" >}}

```bash
ff new --lang=moon hello-world
```

{{< /tab >}}
{{< tab "Lua" >}}

```bash
ff new --lang=lua hello-world
```

{{< /tab >}}
{{< tab "Bitsy" >}}

```bash
ff new --lang=bitsy hello-world
```

{{< /tab >}}
{{< tab "Bulb" >}}

```bash
ff new --lang=bulb hello-world
```

{{< /tab >}}
{{< /tabs >}}

In this example, it will create `hello-world` directory and initialize in it a new app called `hello-world` using your chosen programming language. Don't think about it too hard, you can later change the project name in the config (`hello-world/firefly.toml`).

## 🏃 Build and run

Build the app and launch it in the emulator: `ff run`.

{{< hint info >}}
Have troubles using emulator? Check out the [emulator user guide]({{< ref "/dev/emulator/" >}}).
{{< /hint >}}

## 📦 Distribute

1. Export the app as a ROM (zip file): `ff export`.
1. Publish the file anywhere you like. For open-source projects, a good option is Github Releases.
1. People then can download and install the app:

    ```bash
    ff import ./joearms.hello-world.zip
    ```

1. Optional: add your app into the catalog: [catalog.fireflyzero.com](https://catalog.fireflyzero.com/).

## 🤔 Inspiration

Need inspiration for your next game? Try combining <b id="noun1"></b> and <b id="noun2"></b>.

<script>
  nouns = [
    "battleships",
    "breakout",
    "bullet hell",
    "card game",
    "chess",
    "co-op",
    "cookie clicker",
    "crafting",
    "dungeon crawler",
    "epic explosions",
    "farming simulator",
    "flappy bird",
    "horror",
    "jigsaw puzzle",
    "labyrinth",
    "minesweeper",
    "minigolf",
    "multiplayer", "multiplayer",
    "murder mystery",
    "open world",
    "pacman",
    "pinball",
    "platformer",
    "racing game",
    "realistic physics",
    "roguelike",
    "shooter",
    "snake",
    "space invaders",
    "sudoku",
    "survival game",
    "tamagotchi",
    "teleportation",
    "tetris",
    "text adventure",
    "turn-based strategy",
    "wordle",
  ]
  getNoun = () => nouns[Math.floor(Math.random() * nouns.length)];

  function suggestIdea() {
    noun1 = getNoun();
    noun2 = getNoun();
    while (noun1 === noun2) {
      noun2 = getNoun();
    }
    document.getElementById('noun1').innerText = noun1;
    document.getElementById('noun2').innerText = noun2;
    return false;
  }

  suggestIdea();
</script>

<a class="book-btn" href="#" onclick="return suggestIdea();">
  🔄 regenerate
</a>

Another cool place for inspiration is [My Famicase Exhibition](https://famicase.com/). It's a gallery of covers (with a short description) created for non-existing games. Wouldn't it be fun to bring one of these games to life?

<a href="#" id="famicaseA" target="_blank">
  <img id="famicaseImg" width=220 height=145 alt="random Famicase image" style="display: block; margin-bottom: 8px"/>
</a>

<script>
  function randFamicomId() {
    const id = Math.floor(Math.random() * 244) + 1;
    return String(id).padStart(3, '0');
  }

  function pickFamicase() {
    const year = Math.floor(Math.random() * 6) + 21;
    const id = randFamicomId();
    const imgUrl = `https://famicase.com/${year}/softs/${id}_s.gif`;
    document.getElementById('famicaseImg').src = imgUrl;
    const infoUrl = `https://famicase.com/${year}/softs/${id}.html`;
    document.getElementById('famicaseA').href = infoUrl;
    return false;
  }

  pickFamicase();
</script>

<a class="book-btn" href="#" onclick="return pickFamicase();">
  🔄 reload
</a>

Also have a look at [our catalog](https://catalog.fireflyzero.com/) to see what other people made and check out [popular games for PICO-8](https://itch.io/games/tag-pico-8).

## 🌱 Ecosystem

This section lists third-party packages that can be useful for making Firefly Zero apps and games. All of these packages are tested to compile to Firefly Zero, be fast, and produce very small binaries.

{{< tabs >}}
{{< tab "Rust" >}}

* [micromath](https://github.com/tarcieri/micromath): Math library featuring fast, safe floating point approximations for common arithmetic operations, trigonometry, 2D/3D vector types, statistical analysis, and quaternions.
* [nalgebra](https://docs.rs/nalgebra/latest/nalgebra/): Linear algebra optimized for computing graphics and physics.
* [firefly-toml](https://github.com/firefly-zero/firefly-toml): A macro for statically parsing `firefly.toml`.

{{< /tab >}}
{{< tab "Go" >}}

* [tinymath](github.com/orsinium-labs/tinymath): The fastest Go math library for constrained environments.
* [firefly-go-math](https://github.com/applejag/firefly-go-math): Go game math library for Firefly Zero. Includes random functions using Firefly Zero random source, Vec2 type, and some other math utils.

{{< /tab >}}
{{< tab "MoonBit" >}}

* [micromath.mbt](https://github.com/applejag/micromath.mbt): Embedded math arithmetic, optimized for small code size at the cost of precision.

{{< /tab >}}
{{< /tabs >}}

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
{{< tab "Odin" >}}

* [SDK source code](https://github.com/firefly-zero/firefly-odin)
* [Learn Odin](https://odin-lang.org/docs/overview/)

{{< /tab >}}
{{< tab "MoonBit" >}}

* [SDK source code](https://github.com/firefly-zero/firefly-moon)
* [SDK API docs](https://mooncakes.io/docs/firefly/firefly)
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
