import hashlib
import requests

# Fetch BIP39 English Word List
def fetch_bip39_english_wordlist():
    url = "https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt"
    response = requests.get(url)
    return response.text.splitlines()

# Validate Mnemonic
def mnemonic_to_entropy(mnemonic, wordlist):
    if not all(word in wordlist for word in mnemonic):
        raise ValueError("Mnemonic contains invalid words")
    
    index_list = [wordlist.index(word) for word in mnemonic]
    bits = sum([index << (i * 11) for i, index in enumerate(reversed(index_list))])
    
    checksum_bits_length = len(mnemonic) // 3
    entropy_bits_length = len(mnemonic) * 11 - checksum_bits_length
    entropy = bits >> checksum_bits_length
    
    entropy_bytes = (entropy).to_bytes((entropy_bits_length + 7) // 8, byteorder='big')
    computed_checksum = int.from_bytes(hashlib.sha256(entropy_bytes).digest(), byteorder='big')
    checksum = bits & ((1 << checksum_bits_length) - 1)
    
    if checksum != (computed_checksum >> (256 - checksum_bits_length)):
        raise ValueError("Invalid checksum")
    
    return entropy_bytes

# Fetch the wordlist
BIP39_ENGLISH_WORDLIST = fetch_bip39_english_wordlist()

# Get mnemonic from user
user_mnemonic = input("Please enter your 12-word mnemonic, separated by spaces: ").split()

# Validate the mnemonic
try:
    entropy = mnemonic_to_entropy(user_mnemonic, BIP39_ENGLISH_WORDLIST)
    print("Mnemonic is valid")
except ValueError as e:
    print("Mnemonic is invalid:", str(e))
