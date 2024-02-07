# Activity IV

## 1. (Encryption and Statistical Analysis) Though encryption is primarily designed to preserve confidentiality and integrity of data, the mechanism itself is vulnerable to brute force (statistical analysis). In other words, the more we see the encrypted data, the easier we can hack it. In this exercise, you are asked to crack the following cipher text. Please provide the decrypted result and explain your strategy in decrypting this text.

**Cipher text:** *PRCSOFQX FP QDR AFOPQ CZSPR LA JFPALOQSKR. QDFP FP ZK LIU BROJZK MOLTROE.*

- a. Count the frequency of letters. List the top three most frequent characters
    - P - 7
    - R - 6
    - O - 6
    - F - 6
    - Q - 5
- b. Knowing that this is English, what are commonly used three-letter words and two-letter words. Does the knowledge give you a hint on cracking the given text?
    - Commonly used **three-letter words** in English include 'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'any', 'can', 'had', 'her', 'was', 'one', 'our', 'out', 'day', 'get', 'has', 'him', 'his', 'how', 'man', 'new', 'now', 'old', 'see', 'two', 'way', 'who', 'boy', 'did', 'its', 'let', 'put', 'say', 'she', 'too', 'use'. **Two-letter words** include 'of', 'to', 'in', 'it', 'is', 'be', 'as', 'at', 'so', 'we', 'he', 'by', 'or', 'on', 'do', 'if', 'me', 'my', 'up', 'an', 'go', 'no', 'us', 'am'.
    - This knowledge is beneficial because, in a Caesar cipher, the structure of the language (like common words) is preserved. If we can identify these common structures in the ciphertext, it may give us clues to crack the given text.
- c. Cracking the given text. Measure the time that you have taken to crack this message.
    - Security is the first cause of misfortune. This is an old German proverb.
    - I took about an hour.
- d. Explain your process in hacking such messages.
    - **Frequency Analysis**: I used the frequency of letters in the ciphertext and compare it with the typical frequency of letters in English.
    - **Common Word Structure**: I used common English word structures (like common two or three-letter words) to guess the possible words.
    - **Pattern Recognition**: I tried to recognize patterns in the ciphertext that may correspond to common English words or phrases.
- e. If you know that the encryption scheme is based on Caesar(Monoalphabetic Substitution) that is commonly used by Caesar for sending messages to Cicero, does it allow you to crack it faster?
    - It didn’t help me to crack faster since the monoalphabetic substitution is randomly mapping the plain text alphabet to the cipher text alphabet. Therefore, the methods needed to crack the cipher text are the same which are **Frequency Analysis, Common Word Structure** and **Pattern Recognition**.
- f. Draw a cipher disc of the given text.
    - This is the cipher disc show the mapping between plain alphabet and cipher alphabet. The highlighted yellow cells represent my current best guess for the alphabet mapping based on the given cipher text.
    
    ![Untitled](Activity%20IV%20f4c614422c7248978cc3675532871a75/Untitled.png)
    
- g. Create a simple python program for cracking the Caesar cipher text using brute force attack. Explain the design and demonstrate your software. (You may use an English dictionary for validating results.)
    - The **`brute_force_decrypt_ceasar`** function decrypts a message encrypted with a Caesar cipher by trying all possible shifts, reverses each letter's position in the alphabet by the shift amount, and prints the potential decrypted messages for manual inspection to identify the correct plaintext.
    
    ![Untitled](Activity%20IV%20f4c614422c7248978cc3675532871a75/Untitled%201.png)
    
    - Here is the output
    
    ![Untitled](Activity%20IV%20f4c614422c7248978cc3675532871a75/Untitled%202.png)
    

## 2. (Symmetric Encryption) Vigenère is a complex version of the Caesar cipher. It is a polyalphabetic substitution.

- a. Explain how it can be used to cipher data
    1. **Choose a Keyword**: The length of the keyword can be less than or equal to the length of the plaintext message.
    2. **Extend the key to match the size of input**: The keyword is repeated or truncated to match the length of the plaintext message.
    3. **Encryption Process**: Depending on a position, a same letter may encrypt differently. The encryption of the original text is done using the **Vigenère table**.
- b. If a key is the word “CAT”, please analyze the level of security provided by Vigenère compared to that of the Caesar cipher.
    - For the keyword "CAT", the level of security is increased because:
        - The shift changes for each letter in the plaintext, as determined by the corresponding letter in the keyword.
        - It doesn't just use a single shift for all letters (as in the Caesar cipher), making it more complex and less predictable.
        - However, the security still depends on the length and randomness of the keyword. Short or predictable keywords (like "CAT") can still be vulnerable, especially if the plaintext is long.
- c. Create a python program for ciphering data using Vigenère
    - The code is implemented for the Vigenère cipher, generating a repeated key to match the input text length, encrypting the text by shifting letters based on the key, and providing decryption by inversely shifting the letters.
    
    ```python
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
    ```
    
    ![Untitled](Activity%20IV%20f4c614422c7248978cc3675532871a75/Untitled%203.png)
    

## 3. (Mode in Block Cipher) Block Cipher is designed to have more randomness in a block. However, an individual block still utilizes the same key. Thus, it is recommended to use a cipher mode with an initial vector, chaining or feedback between blocks. This exercise will show you the weakness of Electronic Code Book mode which does not include any initial vector, chaining or feedback

- What does the result suggest about the mode of operation in block cipher?
Please provide your analysis.
    - Encrypting an image in AES-256 ECB mode reveals patterns because of identical plaintext blocks producing identical ciphertext blocks, making it less secure for data with structure. In contrast, AES-256 CBC mode, using an initialization vector and chaining blocks together, disrupts these patterns, making the encrypted image appear as random noise and significantly enhancing security by preventing pattern recognition.

image.png

![image.jpg](Activity%20IV%20f4c614422c7248978cc3675532871a75/image.jpg)

org.pbm

![Untitled](Activity%20IV%20f4c614422c7248978cc3675532871a75/Untitled%204.png)

AES-256-ECB

![Untitled](Activity%20IV%20f4c614422c7248978cc3675532871a75/Untitled%205.png)

AES-256-CBC

![Untitled](Activity%20IV%20f4c614422c7248978cc3675532871a75/Untitled%206.png)

## 4. (Encryption Protocol - Digital Signature)

- a. Measure the performance of a hash function (sha1), RC4, Blowfish and DSA.
Outline your experimental design.
    - Prepare a sample plaintext file of a fixed size for encryption and hashing.
    - Measure the time taken for each operation to complete including SHA1, RC4, Blowfish and DSA
        - SHA1 :
            - Use the OpenSSL command to hash the file with SHA1 and time the operation.
            
            ```bash
            time openssl dgst -sha1 -out hash.sha1 largefile.txt 
            ```
            
        - RC4:
            - Encrypt the sample file using RC4, , noting the time taken.
            
            ```bash
            time openssl enc -rc4 -e -in largefile.txt -out largefile.rc4 -K ebf241a2a4163255ee880f6627ad466c1b5585e6a933c3f07f0dc4eb3c91300d -nopad -nosalt 
            ```
            
        - Blowfish:
            - Encrypt the sample file using Blowfish, , noting the time taken.
            
            ```bash
            time openssl enc -bf -e -in largefile.txt -out [largefile.bf](http://largefile.bf/) -K ebf241a2a4163255ee880f6627ad466c1b5585e6a933c3f07f0dc4eb3c91300d -iv IV -nopad -nosalt 
            ```
            
        - DSA:
            - Generate a DSA key pair.
            - Sign the sample file using the DSA private key and measure the time.
            
            ```bash
            openssl dsaparam -out dsaparam.pem 2048
            openssl gendsa -out privatekey.pem dsaparam.pem
            time openssl dgst -sha1 -sign privatekey.pem -out signature.bin largefile.txt
            ```
            
- b. Comparing performance and security provided by each method.
    - **SHA-1:** Fast but insecure (vulnerable to collisions).
    - **RC4:** Fast but significantly compromised (avoid).
    - **Blowfish:** Good balance of speed and security, but considered older.
    - **DSA:** Relatively slow, but more secure than SHA-1 and RC4. Newer signature schemes like ECDSA might be preferred for better performance and security.
- c. Explain the mechanism underlying Digital Signature. How does it combine the
strength and weakness of each encryption scheme?
    - Digital signatures provide data integrity and authenticity assurance
        - **Sender signs a message using their private key.**
        - **Receiver verifies the signature using the sender's public key.**
    - This ensures both that only the intended receiver can read the message and that they can verify its authenticity and origin.