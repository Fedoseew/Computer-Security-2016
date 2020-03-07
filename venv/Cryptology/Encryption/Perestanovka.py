import random

abc = [chr(i) for i in range(ord('А'), ord('Я') + 1)]  # Наш используемый Алфавит - заглавные русские буквы
key = abc.copy()
random.shuffle(key)
enc = dict(zip(abc,key))
dec = dict(zip(key,abc))
print(enc)
print(dec)
print(dec)