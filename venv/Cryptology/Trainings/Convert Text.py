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
    with open('text3.txt', 'x', encoding='UTF-8') as f:
        f.write(''.join(data2))
    # print(''.join(data2))


convertText(data2)
