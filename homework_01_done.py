# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
       print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4
print(f"Apples: {apples}, Banana: {banana}")

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimeter = storona_1 + storona_2 + storona_3 + storona_4
print("Периметр фігури:", perimeter)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
yabluni = 4
grushi = yabluni + 5
slyvi = yabluni - 2

vsogo_derev = yabluni + grushi + slyvi
print("Всього дерев посадили в саду:", vsogo_derev)

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
do_obidu = 5
pislya_obidu = do_obidu - 10
nadvechir = pislya_obidu + 4

print("Температура надвечір:", nadvechir, "градусів")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""

hlopchykiv = 24
divchatok = hlopchykiv // 2
hlopchykiv_ne_pryishly = 1
divchatok_ne_pryishly = 2

pryjshly = (hlopchykiv - hlopchykiv_ne_pryishly) + (divchatok - divchatok_ne_pryishly)
print("Сьогодні дітей у театральному гуртку:", pryjshly)

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
# Ціни на книжки:
persha = 8
druha = persha + 2
tretia = (persha + druha) / 2

usi = persha + druha + tretia
print("Усі три книжки коштують:", usi, "грн")
