from pathlib import Path
import inspect
import re

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

def read_light_diagram(test=False, filename="input.txt"):
    caller = _caller_dir()
    filename = _resolve_filename(test, filename)

    result = []
    for line in (caller / filename).read_text().splitlines():
        start = line.find('[')
        end = line.find(']')
        if start != -1 and end != -1 and start < end:
            result.append(line[start + 1:end])

    return result

def read_buttons(test=False, filename="input.txt"):
    caller = _caller_dir()
    filename = _resolve_filename(test, filename)

    result = []
    for line in (caller / filename).read_text().splitlines():
        start = line.find(']')
        end = line.find('{')-1
        if start != -1 and end != -1 and start < end:
            result.append( [tuple(map(int, group.split(','))) for group in re.findall(r'\((.*?)\)', line[start + 2:end])])
    return result

def read_joltage(test=False, filename="input.txt"):
    caller = _caller_dir()
    filename = _resolve_filename(test, filename)

    result = []
    for line in (caller / filename).read_text().splitlines():
        start = line.find('{')
        end = line.find('}')
        if start != -1 and end != -1 and start < end:
            result.append(list(map(int,line[start + 1:end].split(","))))

    return result

