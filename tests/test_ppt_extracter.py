import pathlib
from typing import Any

import pytest
import toml

from ppt_extracter import __version__


@pytest.fixture
def base_dir() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parents[1]


@pytest.fixture
def metadata(base_dir: pathlib.Path) -> dict[str, Any]:
    with open(base_dir / "pyproject.toml", "r") as f:
        config = toml.load(f)

    return config["tool"]["poetry"]


def test_version(metadata: dict[str, Any]) -> None:
    version = metadata["version"]
    assert __version__ == version, "Versions do not match"
