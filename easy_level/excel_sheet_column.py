# coding=utf-8
'''
26进制
n为长度
x1*26**(n-1) + x2*26**(n-2) + x3*26**(n-3)

A=1
B=2

Z=26

AA=27
AB=28
AZ=42
BA=43
'''


def excel_columns(s):
    list_s = list(s)
    len_s = len(s) - 1
    columns = 0
    for ele in list_s:
        columns += (ord(ele) % 64) * 26 ** len_s
        len_s -= 1
    return columns


def main():
    for i in ['AA', 'AB', 'BA', 'BC']:
        print excel_columns(i)

if __name__ == '__main__':
    main()
