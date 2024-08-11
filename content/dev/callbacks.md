---
title: 🔔 Callbacks
weight: 10
---

## 🔔 Callbacks

Callback is a function with a specific name that you define in your code and then the runtime calls it in the right time. None of the callbacks are required but you'll need to define at least one of them for your app to actually do something.

## 📚 Supported callbacks

Firefly Zero supports the following callbacks:

1. `boot` is called only once, after all the memory is initialized and all runtime functions are available but before any other callback is called. This is the best place to load fonts, sprites, and other assets, initialize the default state, read configurations, etc.
1. `update` is called ~60 times per second. It is guaranteed to be never called more often, and it won't be called less often if the game doesn't consume too much resources. This is the best place to update the state of objects, position of NPCs, read and handle user input, etc.
1. `render` is called before updating the image on the screen. It might be called less often than `update` if the device sees that the game is slow and needs more resources. This is the best place to call all drawing functions.
1. `render_line` is called before updating a line of pixels on the screen. It accepts the line for each it is called and returns the next line before which it should be called again. For example, it is called with 0 first time and if it then returns 100, it will be called again before rendering the line 100. If then it returns 0, it will be called again only when rendering the next frame. Use it to update the color palette on the fly if you want to display more than 16 colors on one frame.

{{< hint warning >}}
**Use the right callback!**

If you try updating the state from `render`, the game may lag: under load, everything will start moving slower. And even worse, if you only update some state from there, it might lead to state mismatch, like player taking damage before the enemeny even attacks.

Similarly, if you draw on the screen from `update`, you'll be drawing the frame even when it's not shown on the screen, which will spend much more resources than it could.

Remember: update state from `update`, draw things on the screen from `render`.

{{< /hint >}}

This is how you can define a callback:

{{< tabs "define-callback" >}}
{{< tab "🦀 Rust" >}}

```rust
#[no_mangle]
extern fn update() {
    todo!("do something here");
}
```

{{< /tab >}}
{{< tab "🏃 Go" >}}

```go
func init() {
    firefly.Update = update
}

func update() {
    panic("do something here")
}
```

{{< /tab >}}
{{< /tabs >}}

## 🌍 Global state

Almost every app has an internal state (position of NPCs, player's health, etc.), and this state has to be preserved between calls to `update` amd has to be available from `render`. To achieve this, use global variables.

{{< hint info >}}
**Aren't global variables bad?**

It is generally a good idea to avoid a global state. The reason is that it makes testing the code harder. However, it's not the case here: using WebAssembly gives the environment the full control over the app, including its global state. The testing framework that we'll soon implement will allow you to run a unit test for your app and then restore its state to how it was before the test.

So, you can think about Firefly Zero apps more like classes/structs rather than modules, callbacks as methods, and global variables as attributes.
{{< /hint >}}

Here is how to load a font from a file in `boot` and then use it in `render`:

{{< tabs "global-state" >}}
{{< tab "🦀 Rust" >}}

```rust
use firefly_rust::*;
use core::cell::OnceCell;

static mut STATE: OnceCell<State> = OnceCell::new();

struct State {
    font: FileBuf,
}

fn get_state() -> &'static mut State {
    unsafe { STATE.get_mut() }.unwrap()
}

#[no_mangle]
extern fn boot() {
    let state = State {
        font: rom::load_buf("font"),
    };
    unsafe { STATE.set(state) }.ok().unwrap();
}

#[no_mangle]
extern fn render() {
    let state = get_state();
    let font = state.font.as_font();
    draw_text(
        "hello",
        &font,
        Point {x: 20, y: 10},
        Color::Dark,
    );
}
```

{{< /tab >}}
{{< tab "🏃 Go" >}}

```go
package main

import "github.com/firefly-zero/firefly-go/firefly"

var font firefly.Font

func init() {
    firefly.Boot = boot
    firefly.Render = render
}

func boot() {
    font = firefly.LoadROMFile("font").Font()
}

func render() {
    firefly.DrawText(
        "hello",
        font,
        firefly.Point{X: 20, Y: 10},
        ColorDark,
    )
}

```

{{< /tab >}}
{{< /tabs >}}

{{< button relref="./graphics.md" >}}➡️ Graphics{{< /button >}}
