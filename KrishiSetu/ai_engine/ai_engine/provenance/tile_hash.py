Tile-level hashing utilities.

import hashlib
from typing import Dict


def hash_tile(tile: Dict) -> str:
    """Return a stable hash for a tile dictionary."""
    payload = str(sorted(tile.items())).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()
