dict1 = {1: 'aaaaa', 2: 'bbbb', 3: 'ccccccc', 4: 'd', 5: 'eeeeee', 6: 'ffff'}

print(dict1.keys())
print(dict1.values())
print(dict1.items())


def f(e):
    print(e)


print(dict(filter(lambda e: e[0] > 3, dict1.items())))
print(dict(filter(lambda e: len(e[1]) > 3, dict1.items())))

print(list(filter(lambda e: e > 3, dict1.keys())))
print(list(filter(lambda e: len(e) > 4, dict1.values())))
