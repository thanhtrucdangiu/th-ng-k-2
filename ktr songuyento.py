# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 17:41:26 2024

@author: ASUS
"""
import random
def ktr_songuyento (n):
    if n < 2:
        return False
    for i in range (2,n):
        if n % i == 0:
            return False
    return True
songaunhien = random.randint(-99,98)
print ("so ngau nhien duoc tao la", songaunhien)
if ktr_songuyento (songaunhien):
    print ("đó là số nguyên tố")
else:
    print ("đó không phải số nguyên tố")