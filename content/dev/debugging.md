---
title: 🐞 Debugging
weight: 55
params:
  art: /debugging.png
---

This page covers how to find bugs in your apps.

## 😎 Cheat codes

You can add cheat codes to your apps. Cheat codes can be used to put the app into a specific state: jump to a specific level, reset NPCs' positions, set character health, etc.

First, add `[cheats]` table into [`firefly.toml`](./config.md). The table maps cheat code names to numbers that get passed into the app:

```toml
[cheats]
get-health = 1
set-health = 2
```

Next, define the `cheat` callback in the app:

{{< tabs >}}
{{< tab "Rust" >}}

```rust
#[no_mangle]
extern fn cheat(cmd: i32, val: i32) -> i32 {
    match cmd {
        1 => get_health(),
        2 => {
            set_health(val);
            1
        },
        _ => 0,
    }
}
```

{{< /tab >}}
{{< tab "Go" >}}

```go
package main

import "github.com/firefly-zero/firefly-go/firefly"

func init() {
    firefly.Cheat = cheat
}

func cheat(cmd, val int) int {
    switch cmd {
    case 1:
        return getHealth()
    case 2:
        setHealth(val)
        return 1
    default:
        return 0
    }
}
```

{{< /tab >}}
{{< tab "Zig" >}}

```go
pub export fn cheat(cmd: i32, val: i32) i32 {
    switch (cmd) {
        1 => {
            return GetHealth();
        },
        2 => {
            setHealth(val);
            return 1;
        },
        else => {
            return 0;
        }
    }
}
```

{{< /tab >}}
{{< /tabs >}}

Now, you can send cheat codes into a running app using the CLI:

```bash
firefly_cli set-health 56   # prints 1
firefly_cli get-health 0    # prints 56
```

## 🗜 Decompilation

[WebAssembly specification](https://webassembly.github.io/spec/core/) describes 2 file formats: a binary format that Firefly Zero uses and a text format that is human-readable. You can convert the binary format into the text format using the [wasm2wat](https://webassembly.github.io/wabt/doc/wasm2wat.1.html) tool from [wabt](https://github.com/WebAssembly/wabt).

{{< hint info >}}
**Installing wabt**

On Linux, wabt can be installed by running `sudo apt install -y wabt`. For other systems, check out [Github Releases](https://github.com/WebAssembly/wabt/releases/).

Having trouble installing wabt? You can use the [wasm2wat online demo](https://webassembly.github.io/wabt/demo/wasm2wat/) instead.
{{< /hint >}}

For example, here is how to view the text representation of the default launcher's binary:

```bash
wasm2wat --generate-names --fold-exprs \
    $(firefly_cli vfs)/roms/sys/launcher/_bin \
    | less
```

{{< hint info >}}
**When is it useful?**

Looking into the wasm2wat output is useful only for compiled languages and for small binaries. For interpreted languages, like Python, you'll see the code of the interpreter instead of the code of your app. And for big binaries, it's just hard to find in the output what you need. It might be a good idea to create a very small example that reproduces your issue and the decompile it instead.
{{< /hint >}}

## 🔬 Inspection

The `firefly_cli inspect` command shows lots of useful information about the ROM: files, their sizes, metadata, WASM binary sections, elements in them, exported callbacks, imported host functions, etc. For example, to inspect the default system launcher:

```bash
firefly_cli inspect sys.launcher
```

## 💔 Finding the point of failure

When an app explodes (`panic` in Rust and Go, `except` in Python, etc), the runtime logs will tell you in which app callback it happened and what's the last runtime function that was called. In many cases, this is enough to find where the code failed. If it's not, add `log_debug` function calls before and after each line of code that you suspect might fail:

{{< tabs >}}
{{< tab "Rust" >}}

```rust
firefly_rust::log_debug("before foo")
foo()
firefly_rust::log_debug("before bar")
bar()
firefly_rust::log_debug("after bar")
```

{{< /tab >}}
{{< tab "Go" >}}

```go
firefly.LogDebug("before foo")
foo()
firefly.LogDebug("before bar")
bar()
firefly.LogDebug("after bar")
```

{{< /tab >}}
{{< tab "Zig" >}}

```go
const ff = @import("firefly");

ff.logDebug("before foo")
foo()
ff.logDebug("before bar")
bar()
ff.logDebug("after bar")
```

{{< /tab >}}
{{< /tabs >}}

If you see in logs the message printed before the call but not after, your suspicion is correct and you found the point of failure. You can then print values of all variables before the failure to see which input causes the issues.

{{< hint info >}}
**Debugging big functions with "wolf fence" (aka "bisect")**

If there is a lot of code that might be failing, it might be hard to add `log_debug` before every line. In that case, you can do a [binary search](https://en.wikipedia.org/wiki/Binary_search) of the point of failure. First, add one log message in the middle of failing function and run the code. If you see the message, the failure happens after that point. If you don't see, it fails before. Now, insert a message in the middle of the failing region and repeat the process until you find the exact failing line.

This debugging technique is called [Wolf Fence](https://dl.acm.org/doi/pdf/10.1145/358690.358695) or [Bisect](https://research.swtch.com/bisect).
{{< /hint >}}

## 👣 Tracebacks

There are no tracebacks (aka "stack traces" or "back traces") yet. See this issue: [wasmi#538](https://github.com/wasmi-labs/wasmi/issues/538). To find the point of failure, use the debugging techniques covered above.

## 🐌 Monitoring performance

Run `firefly_cli monitor` to launch a dashboard showing the runtime stats for a running app. It looks something like this:

```text
 ┌╴cpu╶───────────────┐ ┌╴memory╶────────────┐
 │ lag      0 ns   0% │ │ floor 1089 KB      │
 │ busy   313 ms  31% │ │ ceil  1152 KB 18p  │
 │ idle   693 ms  69% │ └────────────────────┘
 └────────────────────┘

 ┌╴fuel: update╶──────┐ ┌╴fuel: render╶──────┐
 │ min    276         │ │ min    663         │
 │ max    276         │ │ max    663         │
 │ mean   276         │ │ mean   663         │
 │ stdev    0         │ │ stdev    0         │
 └────────────────────┘ └────────────────────┘
```

* `cpu` shows the CPU usage.
  * `lag` shows the total time (per second) that the app was lagging behind. If it's not zero, the `update` and `render` callbacks are too slow, at least sometimes. Big values may cause visual lag and annoy players. Optimize!
  * `busy` is how much time was spent running code, including system operations.
  * `idle` is how much time the runtime was sleeping and doing nothing. If it's zero, every single update was lagging.
* `memory` shows RAM usage.
  * `floor` shows the position of the last non-zero byte in memory. Depending on the allocator used by the app, it might either show the actual memory usage or mean absolutely nothing.
  * `ceil` is how many memory pages are allocated. One page is 64 KB.
* `fuel` is the number of instructions executed per second.

Keep `lag` zero and `busy`, `memory`, and `fuel` low.

## 💢 Common errors

Below are some of the common errors related to Firefly Zero that you may encounter.

> unsupported compression method 93

You're trying to manually extract a ROM from a ZIP archive created using `firefly_cli export`. ROMs use ZSTD compression that isn't supported by your archive manager. You should use `firefly_cli import` for installing ROMs instead.
