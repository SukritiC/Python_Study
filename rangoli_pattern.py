n = int(input('Enter a size: '))

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for j in range(0, n-1):
    ls_1 = str(''.join(alpha[n-1:abs(n-(j+2)):-1]))
    ls_1 = ls_1 + ls_1[-2::-1]
    ls = str('-'.join(ls_1))
    print('-' * (((n - j) * 2) - 2) + ls + '-' * (((n - j) * 2) - 2))

ls_1 = str(''.join(alpha[n-1::-1]))
ls_1 = ls_1 + ls_1[-2::-1]
ls = str('-'.join(ls_1))
print(ls)

for j in range(n-2, -1, -1):
    ls_2 = str(''.join(alpha[n-1:abs(n-(j+2)):-1]))
    ls_2 = ls_2 + ls_2[-2::-1]
    ls_s = str('-'.join(ls_2))
    print('-' * (((n - j) * 2) - 2) + ls_s + '-' * (((n - j) * 2) - 2))