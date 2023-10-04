import string
from collections import Counter
letters = string.ascii_lowercase
res = ''
with open('tabulka_pocetnosti.txt', 'r') as fp:
    for line in fp:
        lower = line.lower()
        res += lower
        res = res.replace('\n', '')
print(res)
c = Counter(res)
print(c)
for char in letters:
    if char in c:
        print(char.upper(), '-', c[char])
