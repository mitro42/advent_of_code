import json
import __main__
from pathlib import Path
from typing import Any, List, Optional


def input_file_path() -> Path:
    dir = Path(__main__.__file__).parent
    file_name = Path(__main__.__file__).stem + '.txt'
    return dir / file_name


def use_default_file(f):
    def _(file_path: Optional[Path] = None, **kwargs):
        if file_path is None:
            file_path = input_file_path()
        return f(file_path, **kwargs)

    return _


@use_default_file
def string(file_path: Optional[Path] = None) -> str:
    with open(file_path, 'r') as f:
        ret = f.readline()
        return ret


@use_default_file
def strings(
    file_path: Optional[Path] = None,
    sep: Optional[str] = None,
    strip: bool = True,
) -> List[List[str]]:
    with open(file_path, 'r') as f:
        lines = f.readlines()
        if strip:
            lines = [l.strip() for l in lines]
        if sep is not None:
            lines = [l.split(sep) for l in lines]
        return lines


@use_default_file
def numbers(
    file_path: Optional[Path] = None,
    single_line: bool = False,
) -> List[int]:
    with open(file_path, 'r') as f:
        if single_line:
            ret = [int(n) for n in f.readline().split(',')]
        else:
            ret = [int(l.strip()) for l in f.readlines()]
    return ret


@use_default_file
def parse_json(file_path: Optional[Path] = None) -> Any:
    with open(file_path, 'r') as f:
        return json.load(f)
