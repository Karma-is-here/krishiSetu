import hashlib, json

def hash_model(config):
    return hashlib.sha256(
        json.dumps(config, sort_keys=True).encode()
    ).hexdigest()
