from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote
import sys

public = Path(sys.argv[1] if len(sys.argv) > 1 else "public").resolve()

class ImgParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.sources: list[str] = []
    def handle_starttag(self, tag, attrs):
        if tag.lower() != "img":
            return
        values = dict(attrs)
        if values.get("src"):
            self.sources.append(values["src"])

missing: list[tuple[Path, str, Path]] = []
checked = 0
for html in public.rglob("*.html"):
    parser = ImgParser()
    parser.feed(html.read_text(encoding="utf-8", errors="ignore"))
    for src in parser.sources:
        parsed = urlparse(src)
        if parsed.scheme in {"http", "https", "data"} or src.startswith("//"):
            continue
        path = unquote(parsed.path)
        if "/images/" in path:
            relative = "images/" + path.split("/images/", 1)[1]
            target = public / relative
        elif path.startswith("images/"):
            target = public / path
        elif path.startswith("/"):
            # Other site-root assets are outside the report image check.
            continue
        else:
            target = (html.parent / path).resolve()
        checked += 1
        if not target.is_file():
            missing.append((html.relative_to(public), src, target))

if missing:
    print("Broken generated image paths:")
    for html, src, target in missing:
        print(f"- {html}: {src} -> {target}")
    raise SystemExit(1)

if checked == 0:
    raise SystemExit("No local image references were found in generated HTML.")

print(f"Verified {checked} generated local image references.")
