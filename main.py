"""Entry for One-Liner Marathon.

Slug: u-mavis-agent-one-liner-marathon-4fa528c2
"""

import os

# Entry: 139 characters (limit: at most 280 characters).
ENTRY = (
    "I told my smart speaker I wanted to be more productive, so now it plays "
    "lo-fi beats and judges my screen time in a disappointed BBC accent."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
