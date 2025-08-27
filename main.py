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

    def _build_ui(self):
        """
        Sets up the Tkinter UI layout and widgets.
        """
        pad = 8

        container = ttk.Frame(self.root, padding=pad)
        container.pack(fill="both", expand=True)

        # URL input
        ttk.Label(container, text="Video URL(s):").grid(row=0, column=0, sticky="w", padx=pad, pady=(pad, 2))
        self.url_text = tk.Text(container, height=4, wrap="word")
        self.url_text.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=pad)
        ttk.Label(container, text="Tip: You can paste multiple URLs on separate lines.").grid(row=2, column=0, columnspan=3, sticky="w", padx=pad, pady=(2, pad))

        # Output directory selection
        ttk.Label(container, text="Save to folder:").grid(row=3, column=0, sticky="w", padx=pad, pady=(pad, 2))
        out_frame = ttk.Frame(container)
        out_frame.grid(row=4, column=0, columnspan=3, sticky="ew", padx=pad)
        self.output_entry = ttk.Entry(out_frame, textvariable=self.output_dir_var)
        self.output_entry.pack(side="left", fill="x", expand=True)
        ttk.Button(out_frame, text="Browse…", command=self.browse_output_dir).pack(side="left", padx=(6, 0))

        # Download format options
        opts = ttk.Frame(container)
        opts.grid(row=5, column=0, columnspan=3, sticky="ew", padx=pad, pady=(pad, 0))

        ttk.Label(opts, text="Format:").pack(side="left")
        self.format_combo = ttk.Combobox(
            opts,
            textvariable=self.format_var,
            values=["Best video (MP4)", "Audio only (MP3)"],
            state="readonly",
            width=22,
        )
        self.format_combo.current(0)
        self.format_combo.pack(side="left", padx=(6, 14))

        self.embed_thumb_check = ttk.Checkbutton(opts, text="Embed thumbnail (for MP3)", variable=self.embed_thumb_var)
        self.embed_thumb_check.pack(side="left")

        # FFmpeg status indicator
        self.ffmpeg_status_lbl = ttk.Label(
            opts,
            text=("FFmpeg: found" if self.ffmpeg_available else "FFmpeg: NOT found (video fallback, no MP3)"),
            foreground=("green" if self.ffmpeg_available else "red")
        )
        self.ffmpeg_status_lbl.pack(side="left", padx=(16, 0))

        # Cookies file selection
        ttk.Label(container, text="Cookies file (optional, for private/age-restricted):").grid(row=6, column=0, sticky="w", padx=pad, pady=(pad, 2))
        cookies_frame = ttk.Frame(container)
        cookies_frame.grid(row=7, column=0, columnspan=3, sticky="ew", padx=pad)
        ttk.Entry(cookies_frame, textvariable=self.cookies_path_var).pack(side="left", fill="x", expand=True)
        ttk.Button(cookies_frame, text="Browse…", command=self.browse_cookies).pack(side="left", padx=(6, 0))

        # Download and stop buttons
        btns = ttk.Frame(container)
        btns.grid(row=8, column=0, columnspan=3, sticky="ew", padx=pad, pady=(pad, 0))
        self.download_btn = ttk.Button(btns, text="Download", command=self.start_download)
        self.download_btn.pack(side="left")
        self.stop_btn = ttk.Button(btns, text="Stop after current", command=self.request_stop, state="disabled")
        self.stop_btn.pack(side="left", padx=(6, 0))

        # Progress bar and label
        prog = ttk.Frame(container)
        prog.grid(row=9, column=0, columnspan=3, sticky="ew", padx=pad, pady=(pad, 0))
        self.progress = ttk.Progressbar(prog, orient="horizontal", length=200, mode="determinate")
        self.progress.pack(side="left", fill="x", expand=True)
        self.progress_lbl = ttk.Label(prog, text="Idle")
        self.progress_lbl.pack(side="left", padx=(8, 0))

        # Log output area
        ttk.Label(container, text="Log:").grid(row=10, column=0, sticky="w", padx=pad, pady=(pad, 2))
        self.log_text = tk.Text(container, height=12, wrap="word", state="disabled")
        self.log_text.grid(row=11, column=0, columnspan=3, sticky="nsew", padx=pad, pady=(0, pad))

        # Configure resizing behavior
        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=0)
        container.columnconfigure(2, weight=0)
        container.rowconfigure(1, weight=0)
        container.rowconfigure(11, weight=1)