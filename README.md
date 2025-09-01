# Universal Video Downloader

A cross-platform desktop app to download videos and audio from hundreds of social media sites and content platforms, powered by [yt-dlp](https://github.com/yt-dlp/yt-dlp).

## Features

- Download videos or extract audio (MP3) from URLs
- Supports multiple URLs per session
- Simple, user-friendly GUI (Tkinter)
- Progress bar and logging
- Choose output folder
- Optional cookies file for private/age-restricted downloads
- Automatic detection of FFmpeg for audio extraction/merging

## Supported Sites

Supports virtually all major social media and video platforms including:

- YouTube, Facebook, Instagram, Twitter (X), TikTok, Reddit, Vimeo, Dailymotion, SoundCloud, Pinterest, LinkedIn (public videos), Twitch, Likee, VK, Bilibili, Rumble, Odysee, Tumblr, Flickr, Mixcloud, Bandcamp, and many others.

For a full list, see: [yt-dlp Supported Sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)

## Installation

### Prerequisites

- **Python 3.8+** (Recommended: latest Python 3)
- **pip** (Python package manager)
- **FFmpeg** (required for MP3 extraction and best video merging)
- **Tkinter** (usually included with Python, else install separately)

#### Ubuntu/Debian

```bash
sudo apt update
sudo apt install python3 python3-pip python3-tk ffmpeg
```

#### macOS (with Homebrew)

```bash
brew install python3 ffmpeg
```

#### Windows

1. [Download and install Python](https://www.python.org/downloads/windows/)
2. [Download and install FFmpeg](https://ffmpeg.org/download.html)
   - Add `ffmpeg.exe` to your PATH or place it in the app folder.

### Python dependencies

From your project folder:

```bash
pip install -r requirements.txt
```

_Contents of `requirements.txt`:_
```
yt-dlp
```

## Usage

### Run from source

```bash
python3 main.py
```

### Using the GUI

1. Paste one or more video URLs into the "Video URL(s)" field.
2. Choose an output folder.
3. Select format: "Best video (MP4)" or "Audio only (MP3)".
    - **MP3 requires FFmpeg**.
4. (Optional) Add a cookies file for private/age-restricted downloads.
5. Click **Download**.
6. View progress and logs in the app.

## Building Distributables

You can package the app for Windows, Linux, and macOS using [PyInstaller](https://pyinstaller.org/en/stable/):

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

- Executable will be in `dist/`
- Repeat the build process on each OS for native executables.

### Automated Builds

This project uses **GitHub Actions** to automatically build and attach executables for all platforms upon new releases (tagged commits).

- See `.github/workflows/release.yml` for the workflow.
- On pushing a tag (e.g. `v0.1.0-test`), builds for Windows, Linux, and macOS are produced and attached to a draft release.

## Release Process

1. Merge changes to the `stag` branch.
2. Tag the release (e.g., `v0.1.0-test`):  
   ```bash
   git tag v0.1.0-test
   git push origin v0.1.0-test
   ```
3. GitHub Actions builds executables for all platforms.
4. Go to the Releases page, edit the draft release, and publish.

## FFmpeg Note

- **Windows:** Download [ffmpeg](https://ffmpeg.org/download.html) and place `ffmpeg.exe` in your PATH or app folder.
- **Linux/macOS:** Use your package manager (`apt`, `brew`, etc.).

## Contributing

Issues and pull requests are welcome!  
Please test changes on all platforms and document platform-specific quirks.

## License

MIT (see LICENSE file)

---

**Troubleshooting**

- If the app fails to extract MP3 audio, make sure FFmpeg is installed and available in your PATH.
- For site-specific download problems, check yt-dlp's issue tracker or update yt-dlp (`pip install -U yt-dlp`).
- For GUI errors, verify Tkinter is installed (`python3-tk` on Linux).

---

**Credits**

- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [PyInstaller](https://pyinstaller.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)