# Activity V - PKI

[156_Ch07-Activity V-PKI (1).pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/fde18c21-f9ca-47f8-8475-ed54a740baaa/b587adf6-5195-48b3-8af4-9a01cb2960d8/156_Ch07-Activity_V-PKI_(1).pdf)

## 1. From the two given openssl commands, what is the difference?

- The difference between two commands is how the CA certificates are provided for verifying the server’s SSL certificate
    - `openssl s_client -connect [twitter.com:443](http://twitter.com:443/)` : this command uses certificate pre-installed in the computer. This command give a verification status code: 0 (ok) which means it is verified.
    - `openssl s_client -connect [twitter.com:443](http://twitter.com:443/) -CAfile [ca-certificates.cr](http://ca-certificates.cr/)` : this command intends to not providing any certificate for verification. Therefore, it give a verify return code: 20 (unable to get local issuer certificate)

## 2. What does the error (**verify error**) in the first command mean? Please explain.

- When I used OpenSSL to connect to Twitter without specifying trusted certificates, OpenSSL couldn't verify Twitter's identity because it lacked the necessary certificates to trust the connection.

## 3. Copy the server certificate (beginning with -----BEGIN CERTIFICATE----- and
ending with -----END CERTIFICATE-----) and store it as twitter_com.cert. Use
the command **openssl x509 -in twitter_com.cert -text** to show a text
representation of the certificate content. Briefly explain what is stored in an
X.509 certificate (i.e. data in each field).

- Information containing in certificate:
    - **Version:** Shows the certificate format version.
    - **Serial Number:** A unique identifier for the certificate, kind of like a passport number.
    - **Signature Algorithm:** The method used to create the certificate's digital signature, here it's SHA-256 with RSA encryption, ensuring the certificate's authenticity and integrity.
    - **Issuer:** Details about the authority that issued the certificate; in this case, it's DigiCert, a company that verifies and issues digital certificates.
    - **Validity:** Specifies the certificate's valid timeframe, starting from November 2, 2023, to October 31, 2024. It's like an expiration date.
    - **Subject:** Information about the owner of the certificate, here it's Twitter, indicating this certificate is meant for Twitter's website.
    - **Subject Public Key Info:** Contains the public key and the algorithm used (RSA) for encryption, ensuring secure communication with Twitter.
    - **Extensions:** Additional attributes providing various controls and information, like what the certificate can be used for (e.g., server authentication) and alternative names for the website.

## 4. From the information in exercise 3, is there an intermediate certificate? If yes, what purpose does it serve?

- Yes, The intermediate certificate acts as a trusted middle layer between the root CA (the main trusted authority) and Twitter's website certificate, ensuring the security and trustworthiness of the website's encryption.

## 5. Is there an intermediate CA, i.e. is there more than one organization involved in the certification? Say why you think so.

- Yes, there is an intermediate CA. Both the intermediate certificate and the root certificate are issued by the same organization, DigiCert Inc.

## 6. What is the role of ca-certificates.crt?

- It is a bundle of root CA certificates, which mean they are all at the top of the trust chain.

## 7. Explore the ca-certificates.crt. How many certificates are in there? Give the
command/method you have used to count.

```bash

grep -c 'BEGIN CERTIFICATE' ca-certificates.crt
```

- This command searches for the string **`BEGIN CERTIFICATE`** in the **`ca-certificates.crt`** file and counts how many times it appears. Each occurrence represents a single certificate within the bundle.
- `127` certificates

## 8. Extract a root certificate from ca-certificates.crt. Use the openssl command to
explore the details. Do you see any Issuer information? Please compare it to
the details of twitter’s certificate and the details of the intermediate certificate.

- Issuer information of extracted root certificate: **Issuer:** **`CN=ACCVRAIZ1, OU=PKIACCV, O=ACCV, C=ES`**
- **Comparison:**
    - Twitter's certificate and the intermediate certificate form part of a chain of trust, where the intermediate certificate links Twitter's certificate to the root CA in the hierarchy. The root CA is the top chain of trust by the entities relying on the certificate (e.g., web browsers, operating systems), and it validates the entire chain.
    - The extracted root certificate from **`ca-certificates.crt`** (ACCVRAIZ1) is an unrelated root CA that serves as a trustworthiness for other certificates it issues.

## 9. If the intermediate certificate is not in a PEM format (text readable), use the
command to convert a DER file (.crt .cer .der) to PEM file.**openssl x509 -inform der -in certificate.cer -out certificate.pem.**(You need the pem file for exercise 10.)

- Done

## 10. From the given python code, implement the certificate validation.

- Done

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/fde18c21-f9ca-47f8-8475-ed54a740baaa/fa298826-715e-4e77-896c-1ebc3d6f2772/Untitled.png)

## 11. Nowaday, there are root certificates for class 1 and class 3. What uses would a
class 1 signed certificate have that a class 3 doesn't, and vice versa?

- **Main Differences:**
    - **Trust Level**: Class 1 is for when you just need to prove ownership, while Class 3 is for when you need to prove your website or business is safe and trustworthy.
    - **Use Cases**: Use Class 1 for simple, personal sites. Use Class 3 for business sites, especially if you're selling things or need people to trust you with their personal info.
    - **Security**: Class 3 is the way to go for higher security needs, like when you're handling payments or personal details online.

## 12. Assuming that a Root CA in your root store is hacked and under the control
of an attacker, and this is not noticed by anyone for months.

 **1. What further attacks can the attacker stage? Draw a possible attack setup.**

1. **Issuing Fake Certificates:** The attacker can issue valid certificates for any domain they choose. This means they could create a certificate for popular websites like banks, social media platforms, or email services and pretend to be these sites.
2. **Man-in-the-Middle (MITM) Attacks:** The attacker can intercept and decrypt secure communications between users and websites. They could eavesdrop on conversations, steal sensitive information like passwords and credit card numbers, or insert malicious content into the communication stream.
3. **Impersonation:** The attacker could impersonate legitimate websites, leading users to believe they are visiting a secure site when they are actually communicating with a site controlled by the attacker. This could be used for phishing, spreading malware, or fraud.
- **Attack Setup Diagram:**
    - `User <--> Attacker (with fake certificate) <--> Legitimate Website`
1. **In the attack you have described above, can we rely on CRLs or OCSP for protection? Please explain**
    - CRLs (Certificate Revocation Lists) and OCSP (Online Certificate Status Protocol) are mechanisms designed to revoke certificates that are no longer trustworthy, such as when a private key is compromised or a certificate is issued improperly.
    - **CRLs** are lists of certificates that have been revoked before their scheduled expiration dates. CAs publish CRLs at regular intervals.
    - **OCSP** allows applications to check the revocation status of a certificate in real-time by querying the issuing CA.
    - We may not fully rely on the CRLs or OCSP. If the main authority that gives out security certificates (Root CA) is hacked, then the lists and checks (CRLs and OCSP) it uses to tell us which certificates are still good or bad can't be trusted anymore. The hacker could stop bad certificates from being reported or even report good ones as bad.