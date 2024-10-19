# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 17:54:08 2024

@author: ASUS
"""
def tim_phan_tu_list_n(lst, n):
    if n in lst:
        return lst.index(n) # thêm cộng 1 ở đây nếu muốn vị trí số 1 bắt đầu ở 1
    else:
        return None
ds = [1,2,3,4,5] # vị trí 1 tính từ số 0 ví dụ số 1 nằm vị trí 0 nếu muốn bắt đầu ở vị trí số 1 thêm cộng 1
vitri1 = tim_phan_tu_list_n(ds, 1)
vitri2 = tim_phan_tu_list_n(ds, 10)
print("vị trí của 5 là: ", vitri1)
print("vị trí của 10 là: ",vitri2)