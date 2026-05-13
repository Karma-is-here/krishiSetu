Model hash utilities.

import hashlib
from pathlib import Path


def hash_model_file(path: str) -> str:
    """Return SHA256 hash of a model file (empty-safe)."""
    p = Path(path)
    if not p.exists():
        return ""
    data = p.read_bytes()
    return hashlib.sha256(data).hexdigest()
