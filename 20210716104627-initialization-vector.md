---
title: Initialization vector
date: 2021-07-16 10:46
tags:
- 'security'
- 'networking'
---

In [cryptography](20210626145924-cryptography.md), an 
**initialization vector (IV)** or **starting variable (SV)** is an input to a
cryptographic primitive being used to provide the initial state. The IV is
typically required to be random or pseudorandom, but sometimes an IV only needs
to be unpredictable or unique. Randomization is crucial for some encryption
schemes to achieve semantic security, a property whereby repeated usage of the
scheme under the same [key](20210626145712-key-cryptography.md) does not
allow an attacker to infer relationships between (potentially similar) segments
of the encrypted message. For 
[block ciphers](20210716105407-block-cipher.md), the use of an IV is
described by the modes of operation.

[Source](https://en.wikipedia.org/wiki/Initialization_vector)

## What is an initialization vector in layman's terms?

An initialization vector is a chunk of data that is used to scramble a key so
that the key can be re-used but without revealing what the key is. In order for
this to work well it needs to be random or pseudo-random otherwise the IV can be
more easily determined by some malicious 3rd party. Both the receiving and
sending parties know what the IV is, but it's difficult for a 3rd party to
determine what the IV is. The sending and receving side can derive the random IV
by generating it through common state. IV attacks play on weaknesses in the
protocols related to initialization vectors. WEP is a protocol with known IV
weaknesses and it's no longer recommended that be used. 

## Initialization Vector Attack

[WEP](20210613070402-wired-equivalent-privacy.md) was vulnerable to IV
attack. 
