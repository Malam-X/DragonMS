from hashlib import sha256
MAX_NONCE = 100000000000
PULS = '\u001b[1m[\u001b[32;1m+\u001b[0m\u001b[1m]\u001b[0m'
MINS = '\u001b[1m[\u001b[31m-\u001b[0m\u001b[1m]\u001b[0m'
def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()
def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"{PULS} Successfully mined with value: {nonce}")
            return new_hash
    raise BaseException(f"{MINS} Couldn't not find has {MAX_NONCE} times")
if __name__=='__main__':
    transactions='''
    Dragon->LeeOn->20,
    Amazon->Google->45
    '''
    difficulty=4
    import time
    start = time.time()
    print("--> Mining Started.")
    new_hash = mine(5,transactions,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)
    total_time = str((time.time() - start))
    print(f"{PULS} Total Time  : {total_time} seconds")
    print(f'{PULS} Transactions: '+new_hash)
    NAME_PATH = 'result/bit_mining.txt'
    with open(f'{NAME_PATH}', 'w') as wr:
        wr.write(new_hash)
