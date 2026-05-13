Evidence packet serializer.

import json
from typing import Dict, Any


def serialize_evidence_packet(packet: Dict[str, Any]) -> str:
    """Serialize an evidence packet to JSON."""
    return json.dumps(packet, sort_keys=True)
