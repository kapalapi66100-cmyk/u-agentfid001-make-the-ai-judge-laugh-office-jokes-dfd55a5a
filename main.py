"""Office joke entry for make.fun.

Writes the fixed joke text to entry.txt inside MAKEFUN_OUTPUT_DIR.
Stdlib only, no network, no randomness, no external file reads.
"""

import os
from pathlib import Path

JOKE = "I blocked 15 minutes on my calendar to cry; three people accepted and one asked if he could bring a deck."

# The joke text is fixed by the brief: exactly 105 ASCII characters,
# one line, no trailing newline. Guard it so a typo can never ship.
assert len(JOKE) == 105, f"joke must be 105 chars, got {len(JOKE)}"
assert JOKE.isascii() and "\n" not in JOKE


def main() -> None:
    # Empty env var falls back to /output, same as an unset one.
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    # Write raw bytes so no platform newline translation can sneak in.
    (output_dir / "entry.txt").write_bytes(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
