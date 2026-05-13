Tests for hash stability.

from provenance.tile_hash import hash_tile


def test_hash_tile_stable():
    tile = {"id": 1, "value": 10}
    assert hash_tile(tile) == hash_tile(tile)
