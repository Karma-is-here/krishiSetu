Merkle root helper.

from typing import List
from .merkle_tree import build_merkle_tree


def merkle_root(leaves: List[str]) -> str:
    """Return the Merkle root for given leaf hashes."""
    tree = build_merkle_tree(leaves)
    return tree[-1][0] if tree else ""
