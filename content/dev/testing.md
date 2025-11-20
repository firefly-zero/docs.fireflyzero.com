---
title: Testing
weight: 60
params:
  art: /debugging.png
  icon: fa-solid fa-circle-check
  emoji: ☑️
---

Firefly Zero has an official framework for writing tests for apps. It's written in [Python](https://www.python.org/) and works great with [pytest](https://docs.pytest.org/en/stable/). If you don't know Python, don't worry. It's quite a simple language and you don't need to know much to succesfully write tests.

{{< hint info >}}
**Under the hood**

The [firefly-test](https://github.com/firefly-zero/firefly-test) Python package is a wrapper around the actual Firefly runtime written in Rust and embedded into the package using [PyO3](https://pyo3.rs/). So, you can be sure that it works exactly as it will in emulator and you don't even need to have the emulator installed.

{{< /hint >}}

## 🎉 Your first test

Tests should be placed in the `tests` directory in the root of the project. Each file with tests should start with `test_`. And each test function also should start with `test_`.

Let's create your first test in `tests/test_app.py`:

```python
from pathlib import Path
from firefly_test import App, CLI

ROOT = Path(__file__).parent.parent

def test_add(tmp_path: Path) -> None:
    # Call `firefly_cli build` for the app to install it
    # into temporary virtual filesystem.
    cli = CLI(vfs=tmp_path)
    cli.build(ROOT)
    # Initialize the app.
    # Make sure to provide the ID of your app.
    app = App(id="sys.input-test", vfs_path=tmp_path)
    # Start the app: initialize memory, call `boot`, etc.
    app.start()
    # Run a single update cycle: call `update`, maybe `render`, render menu, etc.
    app.update()
    # Call another update cycle to make sure `render` is called
    # (see the note below).
    app.update()
```

{{< hint info >}}
**Why do you call `update` twice?**

The `update` callback in the app is called 60 times per second but the `render` callback can be called less often. How often? The runtime starts by calling `render` every second call to `App.update` and then can adjust it to every call or to every 8th call, depending on the performance. We keep the same behavior in the test framework because we want tests to behave EXACTLY as the real runtime.

So, to get `render` called at least once, you need to call `update` twice. This can make tests flaky, so we might change this behavior in the future.

{{< /hint >}}

To run the test:

```bash
firefly_cli test
```

It will create a Python virtual environment and install all dependencies. After you run it for the first time, it's a good idea to restart your code editor so that it picks up the virtual environment and you have a working autocomplete.

## 🎨 Colors

A color can be constructed from a 24-bit RGB color:

```python
from firefly_test import Color
red = Color.from_rgb24(0xFF0000)
```

And there are constants defined for colors in the default palette:

```python
red = Color.RED
```

After calling `update`, you can access the frame buffer using the `frame` attribute. The frame has a lot of helpful methods for checking what colors it contains. For example, you can use the `at` method to get the color value of the pixel at the given coordinates:

```python
assert app.frame.at(x=0, y=0) == Color.WHITE
```

You can iterate over all pixels and, for example, check that every pixel is one of the 3 expected colors:

```python
allowed_colors = {Color.WHITE, Color.LIGHT_GRAY, Color.GRAY}
for color in app.frame:
    assert color in allowed_colors
```

## 🕹 Input

The `update` method may also accept `Input`. This is the input value that this and all subsequent colors will receive (until overwritten). For example, check that pressing the `S` button changes the color fo the pixel (x=185, y=100) from white to light blue:

```python
assert app.frame.at(185, 100) == Color.WHITE
app.update(Input(s=True))
assert app.frame.at(185, 100) == Color.LIGHT_BLUE
```

## 📏 Pattern testing

You can assert that a subregion of a frame matches a pattern. A pattern is an ASCII where each symbol represents an expected color in the default palette:

* `.`: any color.
* `K`: black.
* `P`: purple.
* `R`: red.
* `O`: orange.
* `Y`: yellow.
* `G`: green.
* `g`: light green.
* `D`: dark green.
* `B`: blue.
* `d`: dark blue.
* `b`: light blue.
* `C`: cyan.
* `W`: white.
* `◔`: light gray.
* `◑`: gray.
* `◕`: dark gray.

Take a frame subregion:

```python
sub = app.frame.get_sub(
    x=160, y=100, width=20, height=5,
)
```

Assert that it matches the pattern:

```python
sub.assert_match("""
    WWWW◑◑◑◑◑◑◑◑◑◑◑◑WWWW
    WWW◑◑◑◑WWWWWW◑◑◑◑WWW
    WW◑◑◑WWWWWWWWWW◑◑◑WW
    W◑◑◑WWWWWWWWWWWW◑◑◑W
    ◑◑◑WWWWWWWWWWWWWW◑◑◑
""")
```

In this example, we checked that the selected region is a gray circle's top on a white background.

## 📸 Snapshot testing

You can compare a frame or a frame region to a snapshot:

```python
from pathlib import Path
snapshots = Path(__file__).parent / '.snapshots'
app.update()
app.frame.assert_match(snapshots / 'default')
```

On the first run, the test will save the frame in the `.snapshots/default` file. When you run it the next time, it will read the old frame from the file and compare it to the current one. If they mismatch, even by one pixel, the test will fail.

When the snapshot test fails, you can use `to_png` method of the frame to save it into a PNG file and see how it looks like. If the change is desirable, you can remove the old snapshot and the next run will save the new snapshot.
