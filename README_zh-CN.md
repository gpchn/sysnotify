# SysNotify

简体中文 | [English](README.md)

SysNotify 是一个轻量级的系统通知工具，旨在简化并增强应用程序的通知管理。

警告：仅在 Windows 10 上测试过。其他平台可能不支持某些功能。

## 功能

- **自定义通知**：轻松创建和管理自定义系统通知。
- **轻量级**：依赖最少，性能优化。
- **易于集成**：简单的 API，可快速集成到您的项目中。

## 安装

### 从 PyPI 安装

```bash
pip install sysnotify
```

### 从源码安装

克隆仓库：

```bash
git clone https://github.com/gpchn/sysnotify.git
cd sysnotify
```

构建 while（使用 `uv`，一个 Python 构建工具。更多详情请访问 [uv 的文档](https://example.com/uv-docs)）：

```bash
uv build
pip install -e dist/sysnotify-1.0.0-py3-none-any.whl
```
> **注意**：将 `[VERSION CODE]` 替换为实际的包版本号，可以在运行 `uv build` 命令后，在 `dist` 目录中找到。

## 使用方法

以下是 SysNotify 的基本使用示例：

```python
import sysnotify

# 显示自定义通知
sysnotify.toast("你好", "这是一个自定义通知")

# 显示信息消息框
sysnotify.msgbox_info("信息", "这是一个信息消息框")

# 显示警告消息框
sysnotify.msgbox_warning("警告", "这是一个警告消息框")

# 显示错误消息框
sysnotify.msgbox_error("错误", "这是一个错误消息框")

# 语音播报消息
sysnotify.say("你好，这是一个语音播报消息")

# 显示横幅
# "横幅" 是一种短时间显示在屏幕角落的消息。
sysnotify.show_banner("这是一个横幅消息")

# 播放系统声音
sysnotify.sys_sound(sysnotify.SystemSound.SYSTEM_ASTERISK)
```

## 贡献

欢迎贡献！请按照以下步骤操作：

1. Fork 这个 repo。
2. 为您的功能或错误修复创建一个新分支。
3. 提交一个包含详细更改描述的 Pull Request。

## 许可证

此项目基于 [MIT 许可证](LICENSE) 发布。

## 联系方式

如有问题或需要支持，请联系 [gpchn](https://github.com/gpchn) 或发送邮件至 [gprogrammer@163.com](mailto:gprogrammer@163.com)。
