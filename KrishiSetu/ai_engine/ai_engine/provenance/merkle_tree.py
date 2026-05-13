Merkle tree construction utilities.

from typing import List
import hashlib


def _hash_pair(a: str, b: str) -> str:
    return hashlib.sha256((a + b).encode("utf-8")).hexdigest()


def build_merkle_tree(leaves: List[str]) -> List[List[str]]:
    """Build a Merkle tree from leaf hashes and return levels."""
    if not leaves:
        return []
    level = leaves[:]
    tree = [level]
    while len(level) > 1:
        next_level = []
        for i in range(0, len(level), 2):
            a = level[i]
            b = level[i + 1] if i + 1 < len(level) else level[i]
            next_level.append(_hash_pair(a, b))
        level = next_level
        tree.append(level)
    return tree
