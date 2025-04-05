# SysNotify

[简体中文](README_zh-CN.md) | English

SysNotify is a lightweight system notification tool designed to streamline and enhance notification management for your applications.

Warning: Only tested on Windows 10. Other platforms may not support some functions.

## Features

- **Custom Notifications**: Easily create and manage custom system notifications.
- **Lightweight**: Minimal dependencies and optimized for performance.
- **Easy Integration**: Simple API for quick integration into your projects.

## Installation

### From PyPI

```bash
pip install sysnotify
```

### From Source

Clone the repository:

```bash
git clone https://github.com/gpchn/sysnotify.git
cd sysnotify
```

Build while (use `uv`, a Python build tool. For more details, visit [uv's documentation](https://example.com/uv-docs)):

```bash
uv build
pip install -e dist/sysnotify-1.0.0-py3-none-any.whl
```

> **Note**: Replace `[VERSION CODE]` with the actual version code of the package, which can be found in the `dist` directory after running the `uv build` command.

## Usage

Here's a basic example of how to use SysNotify:

```python
import sysnotify

# Show a custom notification
sysnotify.toast("Hello", "This is a custom notification")

# Show an info message box
sysnotify.msgbox_info("Info", "This is an info message box")

# Show a warning message box
sysnotify.msgbox_warning("Warning", "This is a warning message box")

# Show an error message box
sysnotify.msgbox_error("Error", "This is an error message box")

# Speak a message
sysnotify.say("Hello, this is a spoken message")

# Show a banner
# A "banner" is a message that is displayed in the corner of the screen for a short period of time.
sysnotify.show_banner("This is a banner message")

# Play a system sound
sysnotify.sys_sound(sysnotify.SystemSound.SYSTEM_ASTERISK)
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or support, please contact [gpchn](https://github.com/gpchn) or email me at [gprogrammer@163.com](mailto:gprogrammer@163.com).
