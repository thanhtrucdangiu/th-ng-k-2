# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 17:37:04 2024

@author: ASUS
"""
def kiem_tra_chuoi_palindrome(s):
    s = s.replace(" ", "").lower()
    if s == s[::-1]:
        return True
    else:
        return False
chuoi1 = "hello"
chuoi2 = "madam"
if kiem_tra_chuoi_palindrome(chuoi1):
    print(f'"{chuoi1}" là chuỗi Palindrome')
else:
    print(f'"{chuoi1}" không phải là chuỗi Palindrome')
if kiem_tra_chuoi_palindrome(chuoi2):
    print(f'"{chuoi2}" là chuỗi Palindrome')
else:
    print(f'"{chuoi2}" không phải là chuỗi Palindrome')