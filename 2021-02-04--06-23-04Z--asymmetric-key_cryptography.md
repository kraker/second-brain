---
title: Public-key cryptography
date: 2021-02-04 06:23
---

**Public-key cryptography**, or **asymmetric cryptography**, is a cryptographic
system that uses pairs of [keys](2021-06-26--14-57-12Z--key_cryptography.md):
_public keys_ (which may be known to others), and _private keys_ (which may
never be known by any except the owner). The generation of such key pairs
depends on [cryptographic](2021-06-26--14-59-24Z--cryptography.md) 
[algorithms](2021-06-26--15-00-51Z--algorithm.md) which are based on
mathematical problems termed [one-way functions](2021-06-26--15-02-20Z--one-way_function.md).
Effective security requires keeping the private key private; and the public key
can be openly distributed without compromising security.
[Source](https://en.wikipedia.org/wiki/Public-key_cryptography)

## Description

[Symmetric-key encryption](2021-02-03--07-29-17Z--symmetric-key_encryption.md) 
has one serious weakness: anyone who gets a hold of the key can encrypt or
decrypt data with it. We're forced to send the key to the recipient in one way 
or another. 

One solution to this problem, is to use two different keys. One to encrypt and
one to decrypt. 

* Public-key cryptography
	+ Two keys generated, public & private
	+ Data encrypted with the public key, requires the private key for decryption
		and vice versa.
	+ Today this works by encrypting a symmetric key with a public key and then
		decrypting the symmetric key with a private key.
	+ [RSA](2021-06-27--07-00-34Z--rsa_cryptosystem.md) is the most common implementation
