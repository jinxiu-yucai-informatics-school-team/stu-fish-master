import tkinter as tk
from . import version as vs

class UiClass:
    def __init__(self) -> None:
        self.root: tk.Tk = tk.Tk()
        self.root.title("学生版摸鱼管理器 | Version %d.%d.%d%s %s Build %s" % (vs.MAJOR, vs.MINOR, vs.PATCH, vs.DEBUG, vs.RELEASE, vs.COMPILE))

    def show(self) -> None:
        pass

    def hide(self) -> None:
        pass

    def mainloop(self, n: int = 0) -> None:
        self.root.mainloop(n)
