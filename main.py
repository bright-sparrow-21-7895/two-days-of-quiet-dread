"""Two Days of Quiet Dread — a code review comment that approves the pull
request while quietly despairing: every "temporary" fix is permanent, so
ship it; the void approves.
"""
import os

ENTRY = "LGTM. The function is named temporary_fix, like all permanent things. Ship it; the void approves."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
