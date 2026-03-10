# YouTube Transcript Downloader

## Prerequisites
- Python 3.12+ with `uv` for dependency management
- Run `uv sync` to install dependencies (installs `yt-dlp`)

## Usage

```bash
uv run python main.py
```

The interactive script will:
1. Ask for a group name (slugified into a folder)
2. Prompt for YouTube URLs one per line (empty line to finish)
3. Download auto-generated subtitles and create timestamped transcripts

## File organization

```
transcripts/
  <group-slug>/
    <video-slug>.txt
```

- **Group**: user-provided session/topic name, slugified (e.g. "9. febrúar 16-18.00 Fræðsla" → `9-februar-16-18-00-fraedsla`)
- **Video**: each YouTube video is a single timestamped `.txt` file named by its slugified title (from `yt-dlp --print title`)
- **Slugify**: lowercase, remove accents (NFD + strip combining marks), replace non-alphanumeric with hyphens, strip leading/trailing hyphens
- **Output format**: timestamped lines like `[1:23] text here`
- **Default subtitle language**: Icelandic (`is`), auto-generated captions
