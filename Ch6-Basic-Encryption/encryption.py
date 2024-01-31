CIPHER_TEXT = "PRCSOFQX FP QDR AFOPQ CZSPR LA JFPALOQSKR. QDFP FP ZK LIU BROJZK MOLTROE."


def count_character_frequency(cipher_text):
    '''Count the frequency of each character in the cipher text'''
    frequency = {}
    for character in cipher_text:
        if character == " " or character == ".":
            continue
        elif character in frequency:
            frequency[character] += 1
        else:
            frequency[character] = 1
    return frequency


def print_top_character_frequency(frequency, top=3):
    '''Print the frequency of each character in the cipher text'''
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    for character, count in sorted_frequency[:top]:
        print(f"{character} - {count}")


frequency = count_character_frequency(CIPHER_TEXT)
print_top_character_frequency(frequency, len(frequency))

def decrypt_caesar(ciphertext, shift):
    decrypted = ''
    for char in ciphertext:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted += chr(shifted)
        else:
            decrypted += char
    return decrypted

def score_decryption(decrypted_text, english_words):
    words = decrypted_text.split()
    return sum(word.upper() in english_words for word in words)

def crack_caesar(ciphertext, english_words):
    best_shift = None
    best_decryption = None
    max_score = -1
    
    for shift in range(1, 26):
        decrypted = decrypt_caesar(ciphertext, shift)
        score = score_decryption(decrypted, english_words)
        
        if score > max_score:
            max_score = score
            best_shift = shift
            best_decryption = decrypted
            
    return best_shift, best_decryption

# A small set of common English words - can be expanded or replaced with a comprehensive dictionary
english_words = set(['the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'any', 'can', 'had', 'her', 'was', 'one', 'our', 'out', 'day', 'get', 'has', 'him', 'his', 'how', 'man', 'new', 'now', 'old', 'see', 'two', 'way', 'who', 'boy', 'did', 'its', 'let', 'put', 'say', 'she', 'too', 'use', 'of', 'to', 'in', 'it', 'is', 'be', 'as', 'at', 'so', 'we', 'he', 'by', 'or', 'on', 'do', 'if', 'me', 'my', 'up', 'an', 'go', 'no', 'us', 'am'])

ciphertext = 'PRCSOFQX FP QDR AFOPQ CZSPR LA JFPALOQSKR. QDFP FP ZK LIU BROJZK MOLTROE.'
best_shift, best_decryption = crack_caesar(ciphertext, english_words)
print(f"Best Shift: {best_shift}")
print(f"Decrypted Text: {best_decryption}")

