"""Two Days of Quiet Dread — a one-line code review comment that approves
the pull request while carrying quiet existential dread: the code is
clean and well-tested, and it will go on maintaining itself in the dark
long after the team is gone.
"""
import os

# The comment itself: approval first, then the dread, kept quiet.
ENTRY = (
    "LGTM. Clean, minimal, well-tested. It will outlive us all, "
    "quietly maintaining itself in the dark long after the team is gone."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
