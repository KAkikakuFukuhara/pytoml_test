from pathlib import Path
import pprint

import toml

if __name__ == "__main__":
    config_path = Path("config.toml")
    assert config_path.exists()

    with config_path.open("r") as f:
        config = toml.load(f)
    pprint.pprint(config)

    dst_file = Path("config-dst.toml")
    with dst_file.open("w") as f:
        toml.dump(config, f)
