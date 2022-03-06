def new_hash(difficulty, height, last_hash, timestamp, nounce, message):
    merkle_root = calculate_merkle_root(message)
    header = "{}{}{}{}{}{}".format(height, last_hash, merkle_root, timestamp, difficulty, nounce)
    intermediary_hash = sha256(header.encode())
    real_hash = sha256(intermediary_hash.hexdigest().encode())
    return real_hash.hexdigest(), merkle_root

def new_block(difficulty, height, last_hash, timestamp, message):
    nounce = 0 
    hash_new = ""

    while hash_new[:difficulty] != "0" * difficulty:
        nounce += 1
        hash_new, merkle_root = new_hash(difficulty, height, last_hash, timestamp, nounce, message)

    new_block = {"difficulty" : difficulty, "height" : height,"merkle_root" : merkle_root, "nonce": nounce,"previous_hash":last_hash,"timestamp":timestamp,"tx":message}
    return new_block