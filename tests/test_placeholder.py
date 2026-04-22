"""Placeholder test — ensures CI passes until real tests are written."""
import pen_compare


def test_version():
    """Verify package has a version attribute."""
    assert hasattr(pen_compare, "__version__")
    assert pen_compare.__version__ == "0.0.1"
