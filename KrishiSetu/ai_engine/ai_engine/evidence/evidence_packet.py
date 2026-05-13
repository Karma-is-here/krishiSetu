Evidence packet construction.

from typing import Dict, Any
from ..crypto.input_hash import hash_input
from ..provenance.merkle_root import merkle_root


def build_evidence_packet(prediction_payload: Dict[str, Any]) -> Dict[str, Any]:
    """Return a minimal evidence packet for a prediction."""
    input_h = hash_input(prediction_payload.get("input"))
    leaf_hashes = prediction_payload.get("tile_hashes", [])
    root = merkle_root(leaf_hashes)
    return {"input_hash": input_h, "merkle_root": root}
