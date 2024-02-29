# Activity III - Log analysis

[162_Ch05-Activity III-Log Analysis.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/fde18c21-f9ca-47f8-8475-ed54a740baaa/45b2dce7-f9ed-4231-a4ee-3950d05a444c/162_Ch05-Activity_III-Log_Analysis.pdf)

## Part I. Can you find people trying to break into the servers?

### 1. How many hackers are trying to get access to our servers? And how many attempts are there?

- The total events within secure.log file are 40,088 events
    - Failed login attempts = 33,253
    - Accepted login attempts = 1,599
- Criteria for identifying potential hackers → Multiple failed login attempts from same IP and the number of attempt is greater than 100

```c
source=*secure.log ("Failed password" OR "invalid user") 
| rex field=_raw "(?<ip_address>\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b)" 
| stats count as attempt_count by ip_address 
| where attempt_count > 100
```

- Number of hacker = 172 hackers

### 2. What time do hackers appear to try to hack our servers?

- 12:15 AM

### 3. Which server (mailsv, www1, www2, www3) seem to see the most attempts?

```c
source=*secure.log ("Failed password" OR "invalid user") 
| top source
```

- www1 has the most attempts. 8,798 attempts.

### 4. What is the most popular account that hackers use to try to break in?

- The account should be valid

```c
source=*secure.log "Failed password for" NOT "invalid user"
| rex field=_raw "Failed password for (?<username>\S+)"
| stats count as attempts by username
| sort - attempts
```

- The most popular account is `root` . 1,493 attempts.

## Part II.  **Sensitive Files on Web Servers**

```c
source=*access.log file="*" | stats count by file
```

### 1. **Can you find attempts to get access to sensitive information from our web servers? How many attempts were there?**

- There are `68` attempts trying to get access to sensitive information which is passwords.pdf

## 2. **What resource/file are hackers looking for?**

- `passwords.pdf`
