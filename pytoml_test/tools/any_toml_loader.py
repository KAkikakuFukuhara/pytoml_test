""" 任意のtomlファイルをロードする
"""
from pathlib import Path
import pprint
from argparse import ArgumentParser

import toml

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("toml", type=str, help="toml file")
    args = parser.parse_args()

    toml_path = Path(args.toml)
    assert toml_path.exists()
    assert toml_path.suffix == ".toml"

    with toml_path.open("r") as f:
        file_data = toml.load(f)
    pprint.pprint(file_data)
