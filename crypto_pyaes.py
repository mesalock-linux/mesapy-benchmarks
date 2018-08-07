#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libs import pyaes

cleartext = "This is a test. What could possibly go wrong? " * 2000 # 92000 bytes

def benchmark():
    # 128-bit key
    key = 'a1f6258c877d5fcd8964484538bfc92c'.decode('hex')
    iv  = 'ed62e16363638360fdd6ad62112794f0'.decode('hex')

    aes = pyaes.new(key, pyaes.MODE_CBC, iv)
    ciphertext = aes.encrypt(cleartext)

    # need to reset IV for decryption
    aes = pyaes.new(key, pyaes.MODE_CBC, iv)
    plaintext = aes.decrypt(ciphertext)

    assert plaintext == cleartext

def main(arg):
    # XXX warmup

    for i in xrange(arg):
        o = benchmark()

if __name__ == "__main__":
    main(100)
