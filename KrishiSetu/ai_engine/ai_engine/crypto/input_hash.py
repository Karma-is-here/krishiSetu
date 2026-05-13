Input hashing utilities.

import hashlib
from typing import Any


def hash_input(payload: Any) -> str:
    """Hash an input payload deterministically."""
    data = repr(payload).encode("utf-8")
    return hashlib.sha256(data).hexdigest()
