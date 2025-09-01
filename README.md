# UD - Video Downloader

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

For a complete list, see: [yt-dlp Supported Sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)

---

## Installation and Running

You can use **standalone executables** (recommended for most users) or run from **Python source code** (for developers/advanced users).

### Option 1: Using Standalone Executable

#### 1. Download Executable

Go to the [GitHub Releases](https://github.com/wahsandaruwan/universal-video-downloader/releases) page and download the file for your platform:
- **Windows:** `main.exe`
- **macOS:** `main`
- **Linux:** `main`

#### 2. Install FFmpeg

- **Windows:**  
  Download [FFmpeg Windows build](https://ffmpeg.org/download.html) and place `ffmpeg.exe` in the same folder as `main.exe` or add to your system PATH.
- **macOS:**  
  Install via Homebrew:  
  ```
  brew install ffmpeg
  ```
- **Linux:**  
  Install via package manager:  
  ```
  sudo apt-get install ffmpeg
  ```

#### 3. Run the Application

- **Windows:** Double-click `main.exe` or run from Command Prompt.
- **macOS/Linux:**  
  Open Terminal, navigate to the folder and run:
  ```
  chmod +x main
  ./main
  ```

---

### Option 2: Run from Python Source Code

#### Prerequisites

- **Python 3.8+**
- **pip**
- **FFmpeg**
- **Tkinter** (usually included; if not, see below)

#### Install Dependencies

From your project folder:
```bash
pip install -r requirements.txt
```
_Contents of `requirements.txt`:_
```
yt-dlp
```

#### Install FFmpeg

(See instructions above per platform.)

#### Install Tkinter

- **Linux:**  
  ```
  sudo apt-get install python3-tk
  ```
- **macOS:**  
  Usually included. If missing, install via Homebrew or ensure Python was installed from python.org.
- **Windows:**  
  Included in most Python installers.

#### Run the App

```bash
python main.py
```

---

## Usage

1. Paste one or more video URLs into the "Video URL(s)" field.
2. Choose an output folder.
3. Select format: "Best video (MP4)" or "Audio only (MP3)".
    - **MP3 requires FFmpeg**.
4. (Optional) Add a cookies file for private/age-restricted downloads.
5. Click **Download**.
6. View progress and logs in the app.

---

## Building Distributables (For Developers)

You can package the app for Windows, Linux, and macOS using [PyInstaller](https://pyinstaller.org/en/stable/):

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

- Executable will be in the `dist/` folder.
- Build separately on each OS for native executables.

### Automated Builds with GitHub Actions

This project uses **GitHub Actions** to automatically build and attach executables for all platforms upon new releases (tagged commits).

- See `.github/workflows/release.yml` for the workflow.
- When a new tag is pushed (e.g. `v0.1.1-test`), builds for Windows, Linux, and macOS are produced and attached to a draft release.

#### Example Release Process

1. Merge changes to the `stag` branch.
2. Tag the release:
   ```bash
   git tag v0.1.1-test
   git push origin v0.1.1-test
   ```
3. GitHub Actions builds executables for all platforms.
4. Go to the Releases page, edit the draft release, and publish.

---

## FFmpeg Note

- **Windows:** Download [ffmpeg](https://ffmpeg.org/download.html) and place `ffmpeg.exe` in your PATH or app folder.
- **Linux/macOS:** Use your package manager (`apt`, `brew`, etc.).

---

## Troubleshooting

- **MP3 extraction fails:**  
  Make sure FFmpeg is installed and available in your PATH.
- **GUI errors:**  
  Ensure Tkinter is installed (`python3-tk` on Linux).
- **Executable flagged by antivirus:**  
  PyInstaller executables may cause false positives on Windows; whitelist if necessary.
- **Site-specific download problems:**  
  Check yt-dlp's issue tracker or update yt-dlp (`pip install -U yt-dlp`).

---

## Contributing

Issues and pull requests are welcome!  
Please test changes on all platforms and document platform-specific quirks.

## License

MIT (see LICENSE file)

---

**Credits**

- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [PyInstaller](https://pyinstaller.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)