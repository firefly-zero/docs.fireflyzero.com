---
title: Ecosystem
weight: 65
params:
  art: /multiplayer.png
  icon: fa-solid fa-seedling
  emoji: 🌱
---

This page lists third-party packages that can be useful for making Firefly Zero apps and games. All of these packages are tested to compile to Firefly Zero, be fast, and produce very small binaries.

{{< tabs >}}
{{< tab "Rust" >}}

* [micromath](https://github.com/tarcieri/micromath): Math library featuring fast, safe floating point approximations for common arithmetic operations, trigonometry, 2D/3D vector types, statistical analysis, and quaternions.
* [nalgebra](https://docs.rs/nalgebra/latest/nalgebra/): Linear algebra optimized for computing graphics and physics.

{{< /tab >}}
{{< tab "Go" >}}

* [tinymath](github.com/orsinium-labs/tinymath): The fastest Go math library for constrained environments.
* [firefly-go-math](https://github.com/applejag/firefly-go-math): Go game math library for Firefly Zero. Includes random functions using Firefly Zero random source, Vec2 type, and some other math utils.

{{< /tab >}}
{{< tab "MoonBit" >}}

* [micromath.mbt](https://github.com/applejag/micromath.mbt): Embedded math arithmetic, optimized for small code size at the cost of precision.

{{< /tab >}}
{{< /tabs >}}
