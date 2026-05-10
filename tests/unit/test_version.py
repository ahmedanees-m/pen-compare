"""Basic import and version test for pen-compare scaffolding."""

import pen_compare


def test_version_string():
    assert pen_compare.__version__ == "0.1.0"


def test_version_importable():
    from pen_compare._version import __version__

    assert __version__ == "0.1.0"
