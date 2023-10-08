# MnemonicValidator

A simple, user-friendly Python tool designed to validate Bitcoin BIP-0039 mnemonic phrases. It assists users by checking the integrity and potential usability of recovery seeds in cryptocurrency wallets, thereby enhancing the safety and recoverability of digital assets.

## Algorithm Overview

### BIP-0039 Mnemonic Validation

1. **Fetch BIP-0039 Wordlist:**
   The BIP-0039 English wordlist is fetched, which contains 2048 words used in the mnemonic phrase generation.

2. **User Input:**
   The user inputs a 12-word mnemonic phrase which is to be validated.

3. **Word Validation:**
   Each word in the user input is checked against the BIP-0039 wordlist to ensure that it is a valid word.

4. **Binary Conversion:**
   Each word from the mnemonic is mapped to its index in the wordlist, and subsequently converted to its binary representation.

5. **Checksum Calculation:**
   - The first `ENT/32` bits of the SHA-256 hash of the binary representation of the entropy are used as a checksum, where `ENT` is the length of the entropy in bits.
   - The checksum is appended to the entropy, and the result is split into sections of 11 bits, each mapping to a word in the wordlist, forming the mnemonic phrase.

6. **Checksum Validation:**
   The checksum embedded in the mnemonic is validated against the computed checksum of the entropy to ensure the mnemonic's integrity.

## Usage

1. Ensure you have Python and `requests` library installed.
2. Run the script: `python mnemonic_validator.py`
3. Input your 12-word mnemonic phrase when prompted.
4. The script will validate the mnemonic and output whether it's valid or invalid.

## Security Notice

Always ensure that your environment is secure when using tools related to cryptographic assets. Never share your mnemonic with untrusted parties and always verify the authenticity of tools and software you use.

## License

[MIT License](LICENSE)

