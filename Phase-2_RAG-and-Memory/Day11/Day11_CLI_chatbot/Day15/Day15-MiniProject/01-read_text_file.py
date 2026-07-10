from pathlib import Path

# The sample file lives right next to this script.
SAMPLE = Path(__file__).resolve().parent / "sample_notes.txt"


def write_sample() -> None:
    """Create a small text file to read back later."""
    with open(SAMPLE, "w", encoding="utf-8") as f:
        f.write("Line 1: Chroma stores vectors.\n")
        f.write("Line 2: Embeddings turn text into meaning.\n")
        f.write("Line 3: RAG retrieves, then the LLM answers.\n")


def read_whole_file() -> str:
    """Read the entire file into one string with f.read()."""
   
    with open(SAMPLE, "r", encoding="utf-8") as f:
        return f.read()


def read_as_lines() -> list:
    """Read the file as a list of lines with f.readlines()."""
    with open(SAMPLE, "r", encoding="utf-8") as f:
       
        return f.readlines()


def read_line_by_line() -> None:
    """Loop the file one line at a time - the memory-friendly way for big files."""
    
    with open(SAMPLE, "r", encoding="utf-8") as f:
        for number, line in enumerate(f, start=1):
            print(f"  line {number}: {line.rstrip()}")
write_sample()
print()