# YouTube Transcript Downloader

Interactive CLI tool that downloads auto-generated YouTube subtitles and converts them into clean, timestamped text transcripts. Designed for batch-downloading transcripts organized by group.

## Setup

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
git clone <repo-url>
cd youtube-transcript
uv sync
```

## Usage

```bash
uv run python main.py
```

The script will interactively ask you for:

1. **Group name** — a label for this group of videos (e.g. a lecture series, event, or topic). This becomes the folder name.
2. **YouTube URLs** — paste one URL per line. Press Enter on an empty line when done.

### Example session

```
=== YouTube Transcript Downloader ===

Enter group name: 9. febrúar Fræðsla
Group: 9-februar-fraedsla/

Enter YouTube URLs one per line. Empty line to finish.

URL (1): https://youtu.be/RDcYuJGbkeA
URL (2):

Processing 1 video(s)...

[1/1] https://youtu.be/RDcYuJGbkeA
  Fetching title...
  Title: Landvarðanámskeið   Fræðsla sem upplýsingagjöf og stjórntæki
  Slug:  landvardanamskeid-fraedsla-sem-upplysingagjof-og-stjorntaeki
  Downloading subtitles...
  Done: 1434 entries → landvardanamskeid-fraedsla-sem-upplysingagjof-og-stjorntaeki.txt

All done! Transcripts saved to: transcripts/9-februar-fraedsla/
```

### Output

This produces a single timestamped transcript file:

```
transcripts/
  9-februar-fraedsla/
    landvardanamskeid-fraedsla-sem-upplysingagjof-og-stjorntaeki.txt
```

Each line in the transcript has a timestamp and the spoken text:

```
[0:02] níum níu settingi þannig að þetta er
[0:03] svona smá prufa en þetta virkar alltaf á
[0:06] endanum.
[0:07] >> Já þetta er allavegana komið núna. Mjög gott
...
```

## File structure

```
transcripts/
  <group-slug>/
    <video-slug>.txt
    <video-slug>.txt
```

- **Group** is your provided name, slugified into a folder
- **Video** files are named from the YouTube video title, slugified
- Default subtitle language is Icelandic (`is`)
