---
title: Digital Signatures
date: 2021-02-04T07:32:00Z
---
[Public-key cryptography](20210204062304-asymmetric-key-cryptography.md)
suffers from the risk that the public key might be from someone who isn't who
they say they are. 

A _digital signature_ is a hash of the public key encrypted by the private key.
The person with the matching public key decrypts the digital signature using the
public key, generates their own hash, and compares it to the decrypted hash to
verify it came from the intended sender.
