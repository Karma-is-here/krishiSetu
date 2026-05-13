import hashlib
import numpy as np

def hash_input(window):
    return hashlib.sha256(
        np.asarray(window, dtype="float32").tobytes()
    ).hexdigest()
