def generateKey(string, key):
    '''This function generates the key 
    in a cyclic manner until its length is 
    equal to the length of original text'''
    
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])

    return("" . join(key))

def cipherText(string, key):
    '''This function returns the
    encrypted text generated with the
    help of the key'''

    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))

# This function decrypts the 
# encrypted text and returns 
# the original text
def originalText(cipher_text, key):
    '''This function decrypts the encrypted text'''
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))
 
if __name__ == "__main__":
    string = "HELLOWORLD"
    keyword = "AYUSH"
    key = generateKey(string, keyword)
    cipher_text = cipherText(string,key)
    print(f"Original string: {string}")
    print(f"Key: {key}")
    print("Ciphertext :", cipher_text)
    print("Original/Decrypted Text :", originalText(cipher_text, key))