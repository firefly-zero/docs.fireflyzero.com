---
title: Designing SDKs
weight: 20
params:
  icon: fa-solid fa-ruler
  emoji: 📐
---

When designing a new SDK for Firefly Zero, we follow these principles:

1. **Reduce type convertions**. Try to use the same integer type everywhere. WebAssembly is 32-bit system, so in Rust it will be `i32`. In Go, `len` and slice indexing use `int`, so that's the best "default" type. If the language supports generic constructors, consider using it to automatically cast 8-bit and 16-bit integers to the default integer type. Using 8-bit or 16-bit integer in some types, like `Pad`, would potentially reduce the size of heap allocations, but most of the time these definitions never leave the stack, and in WebAssembly on the stack everything takes at least 32 bit.
1. **Provide type casts**. If the language provides custom type casting, define it for converting `Pad` to `Point` (and back), `Pad` to `DPad`, `Canvas` to `Image`, `Style` to `LineStyle` (and back), etc.
1. **Provide custom types**. While `load_file` can return a raw byte array and `draw_image` can accept any byte array, it's good to provide custom `File` and `Image` types (and other custom types too whenever is possible). Even if the language doesn't provide nominal type safety, a definition like `enemy: Image` is much more descriptive than `Enemy: []byte`.
1. **Host calls are functions**. You can optionally provide `Line` type with `draw` method for the user's convenience. However, there must be always a `draw_line` function, like for any other WebAssembly host call. The idea is that host calls are side-effects and that's how we make it explicit.
1. **Keep the host functions names**. If the host function is called `draw_line`, the SDK function wrapping it must be called `draw_line` (or `drawLine`, or `DrawLine`) too. Don't call it `render_line` or anything else. The called host function names are visible in the runtime error messages and in `firefly_cli inspect`, so it should be easy for the user to map it to the SDK function calls in their code.
1. **Keep consistent type names**. Use the following type names:
    1. Grpahics: `Angle`, `Canvas`, `Color`, `Font`, `Image`, `LineStyle`, `Point`, `RGB`, `Size`, `Style`, `SubImage`.
    1. FS: `File`.
    1. Input: `Pad`, `DPad`, `Buttons`.
    1. Net: `Peer`, `Peers`, `Stash`.
    1. Stats: `Badge`, `Board`, `Progress`.
    1. Shapes: `Shape`, `Line`, `Rect`, `RoundedRect`, `Circle`, `Ellipse`, `Triangle`, `Arc`, `Sector`.
1. **Follow the language style guides**. Follow the naming convention and all the best practice. If there are several competing standards, pick the most commonly used one. Use all possible linters and code formatters.
1. **Keep modules flat**. There should be only 2 public modules: `firefly.audio` with everything related to audio and `firefly` with everything else (and `sudo` if your SDK provides sudo functions). Even though the host runtime defines modules like `graphics`, `misc`, and more, the SDKs' public API shouldn't reflect that structure. Make it fast and easy for users to find and import all they need.
1. **Avoid allocations**. It should be possible to use SDK to write allocation-free apps. For example, in Go, `ReadPad` returns `(Pad, bool)` instead of `*Pad` so it doesn't escape on the heap. In case of reading a file, most users will want it the file be automatically allocated with the correct size, so you should make both possible. For example, the Go version of `LoadFile` accept an optional buffer and if it is `nil`, a new one is automatically allocated. Or in Rust version, there are two implementations: `load_file` and `load_file_buf`.
1. **Optimize (for size)**. You should provide a simple to use API but it must never sacrifice binary size or performance. If someone wants to push the limits of what Firefly Zero can do, they should be able to do that without bypassing the official SDK. However, in many cases, the compiler is smart enough to optimize out unused code branches, so always validate your assumptions.
1. **Keep the arguments order**. The host functions follow strict rules for arguments order. In particular, drawing functions always accept `Point` first and `Style` last. Your wrappers should follow the same order.
1. **Use 32-bit float**. 32-bit float arithmetic is much faster on the device than 64-bit one.
1. **Provide helpers**. Don't stop just at the host function wrappers. Provide everything that a typical game might need. For example, arithmetic operations for `Point`, radial coordinates for `Pad`, or optional integration with a popular 2D math library.
