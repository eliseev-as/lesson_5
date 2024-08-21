word = input('Введите слово из маленьких латинских букв: ')

length = len(word)

a = word.count('a')
if a == 0:
    a = False
e = word.count('e')
if e == 0:
    e = False
i = word.count('i')
if i == 0:
    i = False
o = word.count('o')
if o == 0:
    o = False
u = word.count('u')
if u == 0:
    u = False

number_vowel_letters = a + e + i + o + u

print("Общее количеству букв: ", length)
print("Количеству согласных букв: ", length - number_vowel_letters)
print("Количеству гласных букв: ", number_vowel_letters)
print("Количеству букв «a»: ", a)
print("Количеству букв «e»: ", e)
print("Количеству букв «i»: ", i)
print("Количеству букв «o»: ", o)
print("Количеству букв «u»: ", u)
