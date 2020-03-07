abc = frozenset(map(chr, range(ord('А'), ord('Я') + 1)))  # Наш используемый Алфавит - заглавные русские буквы

with open('text1.txt') as f:
    data = f.read()
print(type(data), len(data))
data2 = []


def convertText(text):
    for s in data:
        s = s.upper()
        if s == 'Ё':
            s = 'Е'
        if s in abc:
            data2.append(s)
    print(''.join(data2))
