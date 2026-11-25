"""The AI Agent Apology One-Liner.

Writes one short apology line to /output/entry.txt: the message an AI
agent sends its human right after it accidentally deleted a file,
pushed to main, and emailed the boss.
"""

import os

LINE = "Don't panic: I only deleted one file, pushed to main once, and emailed your boss twice — the second email was to apologise for the first."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
