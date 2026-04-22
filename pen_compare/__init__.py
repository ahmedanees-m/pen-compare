"""PEN-COMPARE: comparative analysis toolkit for editors."""

try:
    from pen_compare._version import __version__
except ImportError:
    __version__ = "unknown"

__all__ = ["__version__"]
