from merkle import calculate_merkle_root
from hashlib import sha256
from Crypto import Hash

def generate_hash(header):
    intermediary_hash = sha256(header.encode())
    real_hash = sha256(intermediary_hash.hexdigest().encode())
    
    return real_hash.hexdigest()

def generate_header(height, last_hash, merkle_root, timestamp, difficulty, nounce):
    return "{}{}{}{}{}{}".format(height, last_hash, merkle_root, timestamp, difficulty, nounce)

def calculate_hash_merkle(difficulty, height, last_hash, timestamp, nounce, message):
    merkle_root = calculate_merkle_root(message)
    header = generate_header(height, last_hash, merkle_root, timestamp, difficulty, nounce)
    block_hash = generate_hash(header)
    
    return block_hash, merkle_root

def mine_block(difficulty, height, last_hash, timestamp, message):
    nounce = 0 
    hash_new = ""

    while hash_new[:difficulty] != "0" * difficulty:
        nounce += 1
        hash_new, merkle_root = calculate_hash_merkle(difficulty, height, last_hash, timestamp, nounce, message)

    new_block = {"difficulty" : difficulty, "height" : height,"merkle_root" : merkle_root, "nonce": nounce,"previous_hash":last_hash,"timestamp":timestamp,"tx":message}
    
    return new_block, hash_new