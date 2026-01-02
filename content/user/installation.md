---
title: Installation
weight: 5
params:
  art: /hello.png
  icon: fa-solid fa-download
  emoji: 📥
---

## 🐚 CLI

If you have [cargo](https://doc.rust-lang.org/cargo/) (the [Rust](https://www.rust-lang.org/) package manager) installed, you can use it to install firefly-cli:

```bash
cargo install firefly_cli
```

If you don't, install it from binary releases:

{{< tabs >}}
{{< tab "Linux" >}}

1. [Download the latest release](https://github.com/firefly-zero/firefly-cli/releases/latest). You need the one containing `-linux-` in the name. If you don't know which one you need, it's probably the one ending with `-x86_64-unknown-linux-gnu.tar.gz`.
1. Make sure the `~/.local/bin` directory is in your `$PATH`. Open `~/.bashrc` (or `~/.zshrc` if you use zsh) and add at the end the following:

   ```bash
   export PATH=$PATH:~/.local/bin
   ```

1. Extract the binary and place it into your `$PATH`:

   ```bash
   cd ~/Downloads
   tar -xvf ./firefly_cli-*.tar.gz
   mv ./firefly_cli-*/firefly_cli ~/.local/bin
   chmod +x ~/.local/bin/firefly_cli
   ```

1. Verify installation:

   ```bash
   firefly_cli --version
   ```

{{< /tab >}}
{{< tab "OS X" >}}

1. [Download the latest release](https://github.com/firefly-zero/firefly-cli/releases/latest). You need the one ending with `-x86_64-apple-darwin.tar.gz`.
1. Extract the files from the archive.
1. Right-click on `firefly_cli` and select **Open**.
   If it doesn’t open, go to **System Settings > Privacy & Security**.
   Under **Gatekeeper**, a message should appear - press **Open Anyway**.
1. Make sure the `~/.local/bin` directory is in your `$PATH`.

   ```bash
   mkdir -p ~/.local/bin
   echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.zshrc
   source ~/.zshrc
   ```

   (If you’re on macOS Catalina or older, or if you manually switched your shell to bash, use this instead:)

   ```bash
   echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.bash_profile
   source ~/.bash_profile
   ```

1. Assuming the file is downloaded in your `Downloads` folder:

   ```bash
   cd ~/Downloads
   tar -xvf ./firefly_cli-*.tar.gz
   mv ./firefly_cli-*/firefly_cli ~/.local/bin
   chmod +x ~/.local/bin/firefly_cli
   ```

1. Verify the installation:

   ```bash
   firefly_cli --version
   ```

{{< /tab >}}
{{< tab "Windows" >}}

1. [Download the latest release](https://github.com/firefly-zero/firefly-cli/releases/latest). You need the one containing `-windows-` in the name. If you don't know which one you need, it's probably the one ending with `-x86_64-pc-windows-msvc.zip`.
1. Extract files from the archive.
1. Open the terminal and use the `cd` command to go to the directory containing `firefly_cli`.
1. Verify intallation:

   ```bash
   firefly_cli --version
   ```

{{< /tab >}}
{{< /tabs >}}

## 🚀 Launcher and games

The `firefly_cli import` command can be used to install any app from the [catalog](https://catalog.fireflyzero.com/). Start by installing the default launcher, multiplayer UI, and the snake game:

```bash
firefly_cli import sys.launcher
firefly_cli import sys.connector
firefly_cli import lux.snek
```

## 💻 Emulator

{{< tabs >}}
{{< tab "Linux" >}}

1. [Download the latest release](https://github.com/firefly-zero/firefly-emulator-bin/releases/latest). You need the one ending with `-x86_64-unknown-linux.tgz.gz`.
1. Make sure the `~/.local/bin` directory is in your `$PATH`. Open `~/.bashrc` (or `~/.zshrc` if you use zsh) and add at the end the following:

   ```bash
   export PATH=$PATH:~/.local/bin
   ```

1. Extract the binary and place it into your `$PATH`:

   ```bash
   cd ~/Downloads
   tar -xvf ./firefly-emulator-*.tgz.gz
   mv ./firefly-emulator ~/.local/bin
   chmod +x ~/.local/bin/firefly-emulator
   ```

1. Launch the emulator: `firefly-emulator`

{{< /tab >}}
{{< tab "OS X" >}}

1. [Download the latest release](https://github.com/firefly-zero/firefly-emulator-bin/releases/latest). You need the one ending with `-x86_64-apple-darwin.tgz`.
1. Extract files from the archive.
1. Right click on `firefly_emulator` and press `Open`.

{{< /tab >}}
{{< tab "Windows" >}}

1. [Download the latest release](https://github.com/firefly-zero/firefly-emulator-bin/releases/latest). You need the one ending with `-pc-windows-msvc.tgz`.
1. Extract files from the archive.
1. Double-click on `firefly_emulator`.

{{< /tab >}}
{{< /tabs >}}
