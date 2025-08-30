"""
Application Entry Point

Starts the Tkinter main loop and application.
"""

from app.core import DownloaderApp
import tkinter as tk
from tkinter import ttk

def main():
    """
    Starts the Tkinter main loop and application.
    """
    root = tk.Tk()
    try:
        style = ttk.Style()
        for candidate in ("vista", "clam", "default"):
            if candidate in style.theme_names():
                style.theme_use(candidate)
                break
    except Exception:
        pass

    app = DownloaderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()