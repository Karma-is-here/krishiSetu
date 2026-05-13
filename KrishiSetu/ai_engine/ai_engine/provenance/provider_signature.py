Mock provider signature utilities.

from typing import Dict


def sign_payload(payload: Dict) -> str:
    """Return a mock signature string for a payload."""
    return "MOCK_SIGNATURE"
