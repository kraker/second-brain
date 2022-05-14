---
title: Symmetric-Key Encryption
date: 2021-02-03 07:29
---
Encryption that uses the same key for both encryption and decryption.

Block Cipher
: Encrypts data in single "chunks." _e.g. 128-bit chunks_

* Data Encryption Standard (DES)
	Uses 64-bit block and 56-bit key
	+ Susceptible to brute force attacks
		- Attempted secure derivatives:
			- 3DES, International Data Encryption Algorithm (IDEA), and Blowfish

Stream Cipher
: Encrypts data on-the-fly a single bit at a time. 

* Revest Cipher 4 (RC4)
	+ Stream cipher
	+ 2001-2013 weaknesses discovered in RC4
	+ Considered insecure and a legacy cipher

* [Advanced Encryption Standard](2021-06-26--14-53-43Z--advanced_encryption_standard.md) (AES)
	+ Block cipher
		- Uses 128-bit block size and 128-, 192-, or 256-bit key size
	+ Very secure and practically uncrackable
	+ Very fast
	+ Not just limited to TCP/IP apps, also TLS
		- Many TCP/IP apps still moving towards adoption

- [ ] Extended markdown support in VimWiki, for example, definitions
