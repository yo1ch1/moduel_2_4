numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_primes = True
for i in range(2, 16):
    for j in range(2, (int(i ** 0.5)+1)):
        if i % j != 0:
            is_primes = True
        else:
            is_primes = False
            break
    if is_primes == True:
        primes.append(i)
    else:
        not_primes.append(i)
print(f'''Простые: {primes}''')
print(f'''Составыне: {not_primes}''')




