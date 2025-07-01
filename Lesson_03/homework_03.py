
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії

alice_in_wonderland = (
    """Would you tell me, please, which way I ought to go from here?"""
    "That depends a good deal on where you want to get to,\" said the Cat.\n"
    "\"I don't much care where - \" said Alice.\n"
    "\"Then it doesn't matter which way you go,\" said the Cat.\n"
    "\" - so long as I get somewhere,\" Alice added as an explanation.\n"
    "\"Oh, you're sure to do that,\" said the Cat, \"if you only walk long enough."
)

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті

print ("Кількість одинарних лапок у тексті:", alice_in_wonderland.count("'"))


# task 03 == Виведіть змінну alice_in_wonderland на друк

print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

chorne_more = 436_402
azovske_more = 37_800
plosha_razom = chorne_more + azovske_more
print("Загальна площа Чорного та Азовського морів:", plosha_razom, "км2")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
tovariv_razom = 375_291
pershyj_ta_dryhij_sklad = 250_449
dryhij_ta_tretij_sklad = 222_950
dryhij_sklad = pershyj_ta_dryhij_sklad + dryhij_ta_tretij_sklad - tovariv_razom
pershyj_sklad = pershyj_ta_dryhij_sklad - dryhij_sklad
tretij_sklad = dryhij_ta_tretij_sklad - dryhij_sklad
print("Кількість товарів на першому складі:",pershyj_sklad)
print("Кількість товарів на другому складі:",dryhij_sklad)
print("Кількість товарів на третьому складі:",tretij_sklad)


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

oplata_misjaz = 1179
kilkist_misjaziv = 1.5 * 12
zagalna_vartist = oplata_misjaz * kilkist_misjaziv
print ("Вартість комп’ютера становить:",zagalna_vartist, "грн")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

#a) 8019 % 8
#b) 9907 % 9
#c) 2789 % 5
#d) 7248 % 6
#e) 7128 % 5
#f) 19224 % 9

print("a) 8019 % 8 =", 8019 % 8)
print("b) 9907 % 9 =", 9907 % 9)
print("c) 2789 % 5 =", 2789 % 5)
print("d) 7248 % 6 =", 7248 % 6)
print("e) 7128 % 5 =", 7128 % 5)
print("f) 19224 % 9 =", 19224 % 9)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

pizza_velyka = 4 * 274
pizza_serednja = 2 * 218
sik = 4 * 35
tort = 1 * 350
voda = 3 * 21
razom = pizza_velyka + pizza_serednja + sik + tort + voda
print("Загальна сума замовлення Іринки:", razom, "грн")
# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

razom_foto = 232
foto_na_storinzi = 8
treba_storinok = ( razom_foto + foto_na_storinzi - 1) // foto_na_storinzi
print("Ігорю знадобиться сторінок:", treba_storinok)

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
vidstan_km = 1600
benzin_100km = 9
bak = 48
treba_benziny = (vidstan_km / 100) * benzin_100km
treba_raziv = (treba_benziny + bak -1) // bak
print ("1) Потрібно бензину:", treba_benziny, "літрів")
print ("2) Потрібно заправок:",int(treba_raziv,))