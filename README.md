# Secure Data Pipeline & Password Security
Basic demonstration of password hashing, security principles, and integrity checks.

## Purpose
This project demonstrates fundamental principles of password security and explains why passwords should never be stored in plaintext. It also includes an integrity check mechanism to verify data consistency.

## What this project does
- **Password Hashing**: Accepts a user password and hashes it using cryptographic functions.
- **Verification**: Verifies password correctness by comparing hashes.
- **Integrity Check**: Scans data files and compares them against stored hashes to detect tampering.

## Security Considerations
- **Plaintext Storage**: Highly insecure; this project demonstrates the transition to hashing.
- **Brute-Force**: Even hashed passwords are vulnerable if they are weak.
- **Non-Root Execution**: The Docker container is configured to run as a non-root user to follow security best practices.

## Troubleshooting & Setup (WSL2 Fixes)
During the development on Windows with WSL2, several environment issues were addressed:

### 1. PowerShell Initialization Error
If Windows PowerShell fails with `InitialSessionState` exceptions, use the **WSL/Ubuntu** terminal profile directly in VS Code.

### 2. DNS Resolution Fix
If Docker cannot pull the base image (`python:3.11-slim`) due to `connection refused` on DNS lookups:
```bash
sudo rm /etc/resolv.conf
sudo bash -c 'echo "nameserver 8.8.8.8" > /etc/resolv.conf'
sudo chattr +i /etc/resolv.conf
```
