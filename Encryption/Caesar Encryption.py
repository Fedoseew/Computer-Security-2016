
abc = [chr(i) for i in range(ord('А'), ord('А') + 32)] # Наш используемый Алфавит - заглавные русские буквы
map4 = {abc[i]: i for i in range(len(abc))}

def Caesar(m,n,text1):
    text2 = [map4[i] for i in text1]
    text3 = [(i+n)%m for i in text2]
    text4 = [abc[i] for i in text3]
    return ''.join(text4)

def encrypt(text):
    m = len(abc)
    n = m // 2
    return Caesar(m,n,text)

def decrypt(text):
    m = len(abc)
    n = m // 2
    return Caesar(m,-n,text)

print('Введите слово для шифрования заглавными русскими буквами: ')
text1 = input()
text2 = encrypt(text1)
print('Зашифрованное слово: ' +text2)
text3 = decrypt(text2)
print('Расшифрованное слово: ' + text3)