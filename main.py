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