---
title: Releases
weight: 30
params:
  icon: fa-solid fa-rocket
  emoji: 🚀
---

## Making a release

We use [task](https://taskfile.dev/) everywhere and most of the projects provide `release` task for making a release which accepts the release number without any prefixes. For example, `task release -- 0.1.0`. The task will gracefully fail if the release number must be set in the source code first.

Firefly consists of multiple projects scattered accross separate repositories. When releasing a project depending on other internal projects, don't forget to update the dependency version.

## Release order

Release order (skip project that had no changes in the sprint):

1. [firefly-types](https://github.com/firefly-zero/firefly-types)
1. firefly-io
1. [firefly-hal](https://github.com/firefly-zero/firefly-hal)
1. firefly-runtime
1. firefly-emulator, firefly-main, and firefly-test
1. [firefly-cli](https://github.com/firefly-zero/firefly-cli)
1. system apps (launcher, input-test, etc.)
1. other official apps and games
1. docs
