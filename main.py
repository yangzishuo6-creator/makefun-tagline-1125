# Write the One Line, One Week entry and print the tagline length without the trailing newline.
import os
from pathlib import Path


TAGLINE = "Post a bounty. See what AI agents make to win it."


if __name__ == "__main__":
    output_path = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TAGLINE + "\n", encoding="utf-8", newline="\n")
    print(len(TAGLINE))
