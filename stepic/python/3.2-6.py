s = input()
a = input()
b = input()

if a in s and a in b:
    print('Impossible')
else:
    count = 0
    while a in s:
        s = s.replace(a, b)
        count += 1

    print(count)
