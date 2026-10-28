from importlib import import_module
from importlib.metadata import version
from pathlib import Path

import tomllib


def test_distribution_version_matches_pyproject() -> None:
    pyproject_path = Path(__file__).resolve().parents[2] / "pyproject.toml"
    with pyproject_path.open("rb") as pyproject_file:
        project = tomllib.load(pyproject_file)
    project_metadata = project["project"]

    package = import_module("hoalu")
    assert package.__name__ == "hoalu"
    assert version(project_metadata["name"]) == project_metadata["version"]
