"""Python Text Processing Assignment Starter Code

This file gives you a basic structure to start working on
text processing with strings and file I/O.

Follow the assignment README for the full requirements.
"""


def read_and_clean_file(filename: str) -> list[str]:
    """Read a text file and return a list of cleaned lines.

    TODO: Implement the cleaning rules from the assignment.
    """
    cleaned_lines: list[str] = []
    # Your code here
    return cleaned_lines


def analyze_text(lines: list[str]) -> None:
    """Analyze text lines and print statistics.

    TODO: Implement word/line/character counts and
    word-frequency analysis from the assignment.
    """
    # Your code here
    pass


def main() -> None:
    """Main entry point for the program."""
    filename = input("Enter the name of the text file: ").strip()

    # TODO: Add error handling if the file does not exist

    # TODO: Call read_and_clean_file and analyze_text using the
    #       assignment requirements.


if __name__ == "__main__":
    main()
