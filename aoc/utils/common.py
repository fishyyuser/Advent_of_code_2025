from pathlib import Path
import inspect

def _caller_dir():
    frame = inspect.stack()[2]
    file_path = Path(frame.filename).resolve()
    return file_path.parent

def read_input(filename="input.txt"):
    caller = _caller_dir()
    return (caller / filename).read_text().strip()

def read_lines(filename="input.txt"):
    caller = _caller_dir()
    return (caller / filename).read_text().splitlines()

def read_ints(filename="input.txt"):
    caller = _caller_dir()
    return list(map(int, (caller / filename).read_text().split()))

def read_grid(filename="input.txt"):
    caller = _caller_dir()
    return [list(line.strip()) for line in (caller / filename).read_text().splitlines()]
