---
title: ▶️ Getting started
weight: 5
---

## 👉 Pick the language

Firefly Zero supports lots of programming languages. For simple apps and games, it's a good idea to stick to what you already know. But if you're ready to learn something new for a better results, there are some recommendations:

1. (⌛ Coming soon) ⚡️ [Zig](https://ziglang.org/) is simple and gives the best performance but you need to be careful to avoid bugs and memory leaks.
1. 🦀 [Rust](https://www.rust-lang.org/) gives performance close to Zig and it's hard to use it wrong, but it's also the most difficult language to learn on the list.
1. 🐹 [Go](https://go.dev/) is slower than Rust or Zig but very simple to use and doesn't have memory leaks.
1. (⌛ Coming soon) More languages.

Subjective comparison:

| Language | Simplicity | Performance | Safety  |
| -------- | ---------- | ----------- | --------|
| ⚡️ Zig    | 💻 3/5     | 🐎 5/5      | 🔓 2/5  |
| 🦀 Rust  | 🔬 1/5     | 🐎 5/5      | 🔒 5/5  |
| 🏃 Go    | 🔨 4/5     | 🐇 4/5      | 🔐 4/5  |

## 📥 Install tools

1. [Install rust and cargo](https://www.rust-lang.org/tools/install): `curl https://sh.rustup.rs -sSf | sh`
1. Install [firefly-cli](https://github.com/firefly-zero/firefly-cli): `cargo install firefly-cli`
1. [Download emulator binary](https://github.com/firefly-zero/firefly-emulator-bin/releases) and put it into `$PATH`.
1. Install [WebAssembly](https://webassembly.org/) compiler for your language:

{{< tabs "install-compiler" >}}
{{< tab "Rust" >}}

```bash
rustup target add wasm32-unknown-unknown
```

{{< /tab >}}
{{< tab "Go" >}}

1. [Install Go](https://go.dev/dl/)
1. [Install TinyGo](https://tinygo.org/getting-started/install/)

{{< /tab >}}
{{< /tabs >}}

## 💻 Create the project

Create an empty project:

{{< tabs "create-project" >}}
{{< tab "Rust" >}}

```bash
cargo new hello-world
cargo add firefly_rust
```

{{< /tab >}}
{{< tab "Go" >}}

```bash
mkdir hello-world
cd hello-world
go mod init hello-world
go get github.com/firefly-zero/firefly-go
echo "package main\n\nfunc main() {}" > main.go
```

{{< /tab >}}
{{< /tabs >}}

Create `firefly.toml` config:

```toml
author_id = "joearms"
app_id = "hello-world"
author_name = "Joe Armstrong"
app_name = "Hello World"
```

Write some code:

{{< tabs "write-code" >}}
{{< tab "Rust" >}}

```rust
#![no_std]
#![no_main]
use firefly_rust::*;

#[no_mangle]
extern fn render() {
    draw_triangle(
        Point { x: 60, y: 10 },
        Point { x: 40, y: 40 },
        Point { x: 80, y: 40 },
        Style {
            fill_color:   Color::Accent,
            stroke_color: Color::Secondary,
            stroke_width: 1,
        },
    );
}
```

{{< /tab >}}
{{< tab "Go" >}}

```go
package main

import "github.com/firefly-zero/firefly-go/firefly"

func init() {
    firefly.Render = render
}

func render() {
    firefly.DrawTriangle(
        firefly.Point{X: 60, Y: 10},
        firefly.Point{X: 40, Y: 40},
        firefly.Point{X: 80, Y: 40},
        firefly.Style{FillColor: 2, StrokeColor: 3, StrokeWidth: 1},
    )
}
```

{{< /tab >}}
{{< /tabs >}}

## 🏃 Build and run

1. Build and install the app: `firefly_cli build`
1. Run the last built app: `firefly_emulator`

## 📦 Distribute

1. Create a file for an installed app:

    ```bash
    firefly_cli export --author joearms --app hello-world
    ```

1. Publish the file anywhere you like. A centralized catalog is coming soon.
1. People then can download and install the app:

    ```bash
    firefly_cli import ./joearms.hello-world.zip
    ```

## 🧠 Further reading

There are several things you should know to make a game:

1. How the runtime works in general. Start by reading about [Callbacks](./callbacks.md) and then go through all other pages in this documentation in order.
1. What functions the SDK for the programming language that you choose provides:
    1. [🦀 Rust](https://docs.rs/firefly-rust/latest/firefly_rust/)
    1. [🏃 Go](https://pkg.go.dev/github.com/firefly-zero/firefly-go)
1. How to make games and what patterns make it easier. We recommend reading [Game Programming Patterns](http://gameprogrammingpatterns.com/contents.html).
