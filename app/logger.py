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