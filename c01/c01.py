#!/usr/bin/python3

charset   = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
rot13rev  = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"

decodedset = str.maketrans(charset,rot13rev)

str = "PyvragFvqrYbtvafNerRnfl@syner-ba.pbz"

translatedstr = str.translate(decodedset)
print(translatedstr)
