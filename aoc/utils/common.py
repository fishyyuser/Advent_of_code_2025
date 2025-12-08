from pathlib import Path
import inspect

def _caller_dir():
    frame = inspect.stack()[2]
    file_path = Path(frame.filename).resolve()
    return file_path.parent

def _resolve_filename(test, filename):
    return "test.txt" if test else filename

def read_input(test=False, filename="input.txt"):
    caller = _caller_dir()
    filename = _resolve_filename(test, filename)
    return (caller / filename).read_text().strip()

def read_lines(test=False, filename="input.txt"):
    caller = _caller_dir()
    filename = _resolve_filename(test, filename)
    return (caller / filename).read_text().splitlines()

def read_ints(test=False, filename="input.txt"):
    caller = _caller_dir()
    filename = _resolve_filename(test, filename)
    return [ tuple(map(int, line.split(","))) for line in (caller / filename).read_text().splitlines()]

def read_grid(test=False, filename="input.txt"):
    caller = _caller_dir()
    filename = _resolve_filename(test, filename)
    return [list(line.strip()) for line in (caller / filename).read_text().splitlines()]

def read_range(test=False, filename="input.txt"):
    caller = _caller_dir()
    filename = _resolve_filename(test, filename)
    return [tuple(map(int, r.split("-"))) for r in (caller / filename).read_text().split(",")]

