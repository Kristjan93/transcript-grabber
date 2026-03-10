# YouTube Transcript Downloader

Interactive CLI tool that downloads auto-generated YouTube subtitles and converts them into timestamped text transcripts, organized by group.

## Why YouTube?



## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

## Getting started

```bash
uv sync
uv run python main.py
```

## Example

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

### Output format

Each line has a timestamp and the spoken text:

```
[0:02] níum níu settingi þannig að þetta er
[0:03] svona smá prufa en þetta virkar alltaf á
[0:06] endanum.
[0:07] >> Já þetta er allavegana komið núna. Mjög gott
...
```

### File structure

```
transcripts/
  <group-slug>/
    <video-slug>.txt
```
