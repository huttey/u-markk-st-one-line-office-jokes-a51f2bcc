"""One-line office joke entry: writes the winning line to /output/entry.txt."""

LINE = "Our printer only jams on documents marked urgent — it can smell fear, and it feeds on deadlines."


def main():
    line = LINE.strip()
    assert 1 <= len(line) <= 199, "entry must be 1-199 characters"
    assert "\n" not in line, "entry must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
