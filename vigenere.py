#!/usr/bin/env python3

def encrypt(plain_text, keys):
    encrypted_text = ''
    for i in range(len(plain_text)):
        encrypted_text += chr(((ord(plain_text[i]) + (ord(keys[i]))) % 26) + 65)

    return encrypted_text.lower()

def decrypt(encrypted_text, keys):
    plain_text = ''
    for i in range(len(encrypted_text)):
        plain_text += chr(((ord(encrypted_text[i]) - (ord(keys[i]))) % 26) + 65)

    return plain_text.lower()
