def odd_or_even(n):
    return '奇數'*(n&1) or '偶數'

a = int(input('輸入數字：'))
b = odd_or_even(a)
print(f'{a}是{b}')

