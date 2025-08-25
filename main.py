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

