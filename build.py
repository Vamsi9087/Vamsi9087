"""Embeds your photos into the animated SVGs.
Usage:  python build.py
Uses photos/hero.jpg (portrait, ~380x480) and photos/card.jpg (~360x386).
Replace those two files to change your picture, then run this again."""
import base64, pathlib
root = pathlib.Path(__file__).parent
b64 = lambda f: base64.b64encode((root / "photos" / f).read_bytes()).decode()
subs = {"HERO_B64": b64("hero.jpg"), "CARD_B64": b64("card.jpg")}
(root / "assets").mkdir(exist_ok=True)
for t in (root / "templates").glob("*.svg"):
    s = t.read_text()
    for k, v in subs.items():
        s = s.replace(k, v)
    (root / "assets" / t.name).write_text(s)
    print("built", t.name)
