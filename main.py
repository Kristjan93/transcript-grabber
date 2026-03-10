import os
import re
import subprocess
import tempfile
import unicodedata


# ANSI colors
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

TRANSCRIPTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "transcripts")


def slugify(text: str) -> str:
    replacements = {"ð": "d", "þ": "th", "æ": "ae", "ö": "o"}
    text = text.lower()
    for orig, repl in replacements.items():
        text = text.replace(orig, repl)
    text = unicodedata.normalize("NFD", text)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return text


def yt_dlp(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["yt-dlp", *args], capture_output=True, text=True)


def parse_srt(content: str) -> list[str]:
    blocks = re.split(r"\n\n+", content.strip())
    entries = []
    prev_text = None
    for block in blocks:
        blines = block.strip().split("\n")
        if len(blines) < 3:
            continue
        text = " ".join(re.sub(r"<[^>]+>", "", l) for l in blines[2:]).strip()
        if not text or text == prev_text:
            continue
        prev_text = text
        match = re.match(r"(\d{2}):(\d{2}):(\d{2})", blines[1])
        if match:
            h, m, s = match.groups()
            ts = f"{int(h)}:{m}:{s}" if int(h) > 0 else f"{int(m)}:{s}"
            entries.append(f"[{ts}] {text}")
    return entries


def process_video(url: str, group_dir: str):
    print(f"  {CYAN}Fetching title...{RESET}")
    result = yt_dlp("--skip-download", "--print", "title", url)
    if result.returncode != 0:
        print(f"  {RED}Failed to fetch video info{RESET}")
        return

    title = result.stdout.strip()
    video_slug = slugify(title)
    print(f"  {CYAN}Title:{RESET} {title}")
    print(f"  {CYAN}Slug:{RESET}  {video_slug}")

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = os.path.join(tmp_dir, "transcript")
        print(f"  {CYAN}Downloading subtitles...{RESET}")
        result = yt_dlp(
            "--write-auto-sub", "--sub-lang", "is", "--sub-format", "srt",
            "--skip-download", "-o", tmp_path, url,
        )
        srt_file = f"{tmp_path}.is.srt"
        if result.returncode != 0 or not os.path.exists(srt_file):
            print(f"  {RED}No subtitles found{RESET}")
            return

        with open(srt_file) as f:
            entries = parse_srt(f.read())

    output_path = os.path.join(group_dir, f"{video_slug}.txt")
    with open(output_path, "w") as f:
        f.write("\n".join(entries))

    print(f"  {GREEN}Done: {len(entries)} entries → {video_slug}.txt{RESET}")


def main():
    print(f"\n{BOLD}{CYAN}=== YouTube Transcript Downloader ==={RESET}\n")

    group = input(f"{YELLOW}Enter group name:{RESET} ").strip()
    if not group:
        print(f"{RED}Group name cannot be empty.{RESET}")
        return

    group_slug = slugify(group)
    group_dir = os.path.join(TRANSCRIPTS_DIR, group_slug)
    os.makedirs(group_dir, exist_ok=True)
    print(f"{GREEN}Group:{RESET} {group_slug}/\n")

    print(f"{YELLOW}Enter YouTube URLs one per line. Empty line to finish.{RESET}\n")

    urls = []
    while True:
        url = input(f"{CYAN}URL ({len(urls) + 1}):{RESET} ").strip()
        if not url:
            break
        urls.append(url)

    if not urls:
        print(f"\n{RED}No URLs provided.{RESET}")
        return

    print(f"\n{BOLD}{GREEN}Processing {len(urls)} video(s)...{RESET}\n")

    for i, url in enumerate(urls, 1):
        print(f"{BOLD}{YELLOW}[{i}/{len(urls)}]{RESET} {url}")
        process_video(url, group_dir)
        print()

    print(f"{BOLD}{GREEN}All done! Transcripts saved to:{RESET} {group_dir}/")


if __name__ == "__main__":
    main()
