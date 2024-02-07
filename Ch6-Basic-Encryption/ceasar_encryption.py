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


def encrypt_text(plaintext,n):
    ans = ""
    # iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]
        
        # check if space is there then simply add space
        if ch==" ":
            ans+=" "
        # check if a character is uppercase then encrypt it accordingly 
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly
        
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    
    return ans

plaintext = "HELLO WORLD"
n = 3
print("Plain Text is : " + plaintext)
print("Shift pattern is : " + str(n))
print("Cipher Text is : " + encrypt_text(plaintext,n))


message = 'KHOOR ZRUOG' #encrypted message
Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def brute_force_decrypt_ceasar(message):
    for key in range(len(Letters)):
        translated = ''
        for symbol in message:
            if symbol in Letters:
                num = Letters.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(Letters)
                translated = translated + Letters[num]
            else:
                translated = translated + symbol
        print('Hacking key #%s: %s' % (key, translated))
        
brute_force_decrypt_ceasar(message)


