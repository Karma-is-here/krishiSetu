import hashlib

def merkle_root(hashes):
    while len(hashes) > 1:
        hashes = [
            hashlib.sha256(
                (hashes[i] + hashes[i+1]).encode()
            ).hexdigest()
            for i in range(0, len(hashes)-1, 2)
        ]
    return hashes[0]
