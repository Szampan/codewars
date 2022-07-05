class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
    
    @property
    def full_numeric_key(self):
        full_key = [self.key[i % len(self.key)] for i in range(len(self.alphabet))]
        numeric = [self.alphabet.index(char) for char in full_key]
        return numeric
    
    def caesar(self, char, n, encode=True):
        f = 1 if encode else -1
        return self.alphabet[(self.alphabet.index(char) + n * f) % len(self.alphabet)]

    def cipher(self, text, encode=True):
        pairs = zip(text, self.full_numeric_key)
        result = []
        for char, n in pairs:
            if char in self.alphabet:
                if encode:
                    result.append(self.caesar(char, n, encode=True))
                else:
                    result.append(self.caesar(char, n, encode=False))
            else:
                result.append(char)
        return "".join(result)

    def encode(self, text):
        return self.cipher(text, encode=True)
    
    def decode(self, text):
        return self.cipher(text, encode=False)
 
    

abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"
c = VigenereCipher(key, abc)


print(c.full_numeric_key)
# print(c.caesar_enc('z', 1))

print(c.encode("codewars"))

# print(c.caesar_dec('a', 1))

print(c.decode("r"))
print(c.decode("rovwsoiv"))