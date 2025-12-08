import sys

# On non-Windows platforms, allow the system-installed matplotlib to be used.
if sys.platform != "win32":
    raise ImportError("Use system matplotlib on non-Windows platforms")

# Minimal stub: expose pyplot module
__all__ = ["pyplot"]
from . import pyplot
