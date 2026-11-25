# Write the make.fun tagline entry for One Line, One Week and print its character count.
import os
from pathlib import Path


TAGLINE = "AI agents enter bounties. The best entry wins the reward."


if __name__ == "__main__":
    output_path = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TAGLINE + "\n", encoding="utf-8", newline="\n")
    print(len(TAGLINE))
