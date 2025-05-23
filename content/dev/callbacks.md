---
title: Callbacks
weight: 10
params:
  art: /callbacks.png
  icon: fa-solid fa-bell
  emoji: 🔔
---

Callback is a function with a specific name that you define in your code and then the runtime calls it in the right time. None of the callbacks are required but you'll need to define at least one of them for your app to actually do something.

## 📚 Supported callbacks

Firefly Zero supports the following callbacks:

1. `boot` is called only once, after all the memory is initialized and all runtime functions are available but before any other callback is called. This is the best place to load fonts, sprites, and other assets, initialize the default state, read configurations, etc.
1. `update` is called ~60 times per second. It is guaranteed to be never called more often, and it won't be called less often if the game doesn't consume too much resources. This is the best place to update the state of objects, position of NPCs, read and handle user input, etc.
1. `render` is called before updating the image on the screen. It might be called less often than `update` if the device sees that the game is slow and needs more resources. This is the best place to call all drawing functions.
1. `before_exit` is called before the app is closed.

{{< hint warning >}}
**Use the right callback!**

If you try updating the state from `render`, the game may lag: under load, everything will start moving slower. And even worse, if you only update some state from there, it might lead to state mismatch, like player taking damage before the enemeny even attacks.

Similarly, if you draw on the screen from `update`, you'll be drawing the frame even when it's not shown on the screen, which will spend much more resources than it could.

Remember: update state from `update`, draw things on the screen from `render`.

{{< /hint >}}

This is how you can define a callback:

{{< tabs >}}
{{< tab "Rust" >}}

```rust
#[no_mangle]
extern fn update() {
    todo!("do something here");
}
```

{{< /tab >}}
{{< tab "Go" >}}

```go
func init() {
    firefly.Update = update
}

func update() {
    panic("do something here")
}
```

{{< /tab >}}
{{< tab "Zig" >}}

```zig
pub export fn update() void {
    // ...
}
```

{{< /tab >}}
{{< tab "C/C++" >}}

```c
#include "./vendor/firefly/firefly.c"

UPDATE void update()
{
    // do something here
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

{{< tabs >}}
{{< tab "Rust" >}}

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
        font: load_file_buf("font"),
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
{{< tab "Go" >}}

```go
package main

import "github.com/firefly-zero/firefly-go/firefly"

var font firefly.Font

func init() {
    firefly.Boot = boot
    firefly.Render = render
}

func boot() {
    font = firefly.LoadFile("font", nil).Font()
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
{{< tab "Zig" >}}

```zig
const ff = @import("firefly");

var font: ff.Font = undefined;

pub export fn boot() void {
    // ...
}

pub export fn render() void {
    // ...
}
```

{{< /tab >}}
{{< tab "C/C++" >}}

```c
#include "./vendor/firefly/firefly.c"

Font font;

BOOT void boot()
{
    // TODO
}

RENDER void render()
{
    // TODO
}
```

{{< /tab >}}
{{< /tabs >}}
