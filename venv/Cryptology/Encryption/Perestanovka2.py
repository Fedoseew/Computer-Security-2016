import random

abc = list(map(chr(i) for i in range(ord('А'), ord('Я') + 1)))  # Наш используемый Алфавит - заглавные русские буквы
key = abc.copy()
random.shuffle(key)
enc = dict(zip(abc, key))
dec = dict(zip(key, abc))
print(enc)
print(dec)


def convert(d, s):
    return ''.join(map(lambda t: d[t], s))


t1 = 'КРИПТОГРАФИЯ'
t2 = convert(enc, t1)
t3 = convert(dec, t2)
print(t1)
print(t2)
print(t3)
