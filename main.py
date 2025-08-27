# Imports
import os
import re
import shutil
import threading
import tkinter as tk
import yt_dlp
from tkinter import ttk, filedialog, messagebox

APP_TITLE = "Universal Video Downloader"
DEFAULT_OUTPUT_DIR = os.path.join(os.path.expanduser("~"), "Downloads")

# ----------- Utility functions -----------

def extract_urls(text: str):
    """
    Extracts URLs from the given text, cleans trailing punctuation,
    and returns a deduplicated list.
    """
    urls = re.findall(r'https?://\S+', text, re.IGNORECASE)
    cleaned = []
    for u in urls:
        cleaned.append(u.rstrip('),.]\'}"'))
    seen = set()
    result = []
    for u in cleaned:
        if u not in seen:
            seen.add(u)
            result.append(u)
    return result

def is_ffmpeg_available() -> bool:
    """
    Checks if ffmpeg is available on the system PATH.
    Returns True if found, False otherwise.
    """
    return shutil.which("ffmpeg") is not None

# ----------- Logger for yt-dlp -----------

class TkLogger:
    """
    Logger class to redirect yt-dlp log outputs to the Tkinter UI.
    """
    def __init__(self, write_fn):
        self.write_fn = write_fn

    def debug(self, msg):
        txt = str(msg)
        if any(key in txt.lower() for key in ["error", "warning", "extractor"]):
            self.write_fn(txt)

    def info(self, msg):
        self.write_fn(str(msg))

    def warning(self, msg):
        self.write_fn(f"Warning: {msg}")

    def error(self, msg):
        self.write_fn(f"Error: {msg}")

# ----------- Main Application Class -----------

class DownloaderApp:
    """
    Main desktop application class for video downloading.
    Manages UI, user actions, and download logic.
    """
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry("820x580")
        self.root.minsize(720, 540)

        self.downloading = False
        self.stop_requested = False
        self.ffmpeg_available = is_ffmpeg_available()

        # UI variables
        self.output_dir_var = tk.StringVar(value=DEFAULT_OUTPUT_DIR)
        self.format_var = tk.StringVar(value="Best video (MP4)")
        self.embed_thumb_var = tk.BooleanVar(value=True)
        self.cookies_path_var = tk.StringVar(value="")

        self._build_ui()