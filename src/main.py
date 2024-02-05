import api.v1
import api.v1.version as vs

import sys
import tkinter as tk

def main(argc: int, argv: list[str]) -> int:
    app: api.v1.uiclass.UiClass = api.v1.uiclass.UiClass()
    app.mainloop()

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
