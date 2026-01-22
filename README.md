# password-security-basics
Basic demonstration of password hashing and security principles
## Purpose
This project demonstrates fundamental principles of password security and explains why passwords should never be stored in plaintext.

## What this project does
- Accepts a user password as input
- Hashes the password using a cryptographic hash function
- Verifies password correctness by comparing hashes

## Security considerations
- Plaintext password storage is highly insecure
- Hashing reduces the risk of password disclosure
- Weak passwords remain vulnerable to brute-force attacks

## What I learned
- Difference between plaintext and hashed passwords
- Basic password-related security risks
- Importance of secure authentication mechanisms

## Possible improvements
- Add salting
- Add password strength validation
- Compare different hashing algorithms

## Running with Docker

This project can be executed inside a Docker container to provide
a consistent and isolated runtime environment

### Build the Docker image
```bash
docker build -t password-security

This container is configured to run as a non-root user in order to
follow Docker security best practices and reduce potential attack impact.
