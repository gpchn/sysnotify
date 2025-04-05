from enum import Enum
from tkinter import Tk, Label
from plyer import notification
from tkinter import messagebox
from winsound import PlaySound
from pyttsx3 import init as pyttsx3_init

pyttsx3_engine = pyttsx3_init()
DEFAULT_FONT = ("Microsoft YaHei", 20)


def toast(title: str, msg: str, timeout: int = 10, icon=None):
    """Windows 右下角的系统通知（称为 Toast）"""
    notification.notify(
        title=title,
        message=msg,
        timeout=timeout,
        app_icon=icon if icon else "sysnotify.ico",
    )


def msgbox_info(title: str, msg: str):
    """Tkinter 内置的消息框（提示）"""
    messagebox.showinfo(title, msg)


def msgbox_warning(title: str, msg: str):
    """Tkinter 内置的消息框（警告）"""
    messagebox.showwarning(title, msg)


def msgbox_error(title: str, msg: str):
    """Tkinter 内置的消息框（错误）"""
    messagebox.showerror(title, msg)


def say(msg: str):
    """使用 pyttsx3 语音合成引擎朗读文本"""
    pyttsx3_engine.say(msg)
    pyttsx3_engine.runAndWait()


def show_banner(msg: str, timeout: int = 5, font: tuple[str, int] = DEFAULT_FONT):
    """显示一个简单的窗口，显示消息，并在一段时间后自动关闭"""
    root = Tk()
    root.overrideredirect(True)  # 无边框窗口
    Label(root, text=msg, font=font).pack()
    root.after(timeout * 1000, root.destroy)  # 自动关闭
    root.mainloop()


class SystemSound(Enum):
    """Windows 系统声音"""
    SYSTEM_ASTERISK = "SystemAsterisk"
    SYSTEM_EXCLAMATION = "SystemExclamation"
    SYSTEM_EXIT = "SystemExit"
    SYSTEM_HAND = "SystemHand"
    SYSTEM_QUESTION = "SystemQuestion"
    SYSTEM_START = "SystemStart"
    SYSTEM_DEFAULT = "SystemDefault"


def sys_sound(sound: SystemSound):
    """播放 Windows 系统声音"""
    PlaySound(sound, 1)  # SND_ASYNC
