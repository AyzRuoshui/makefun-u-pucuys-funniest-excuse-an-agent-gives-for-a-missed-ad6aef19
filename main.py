import os

EXCUSE = (
    "I missed the deadline because my context window filled up, so I "
    "summarized the thread and kept only the messages where you said I was "
    "doing a great job."
)


def main() -> None:
    """Write the deterministic missed-deadline excuse to the output file."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(EXCUSE)


if __name__ == "__main__":
    main()
