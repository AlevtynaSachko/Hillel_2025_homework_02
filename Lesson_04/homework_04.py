adventures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

#помилка в оригінальній назві, в слові adventures

adventures_of_tom_sawer = ("""\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth.""" )
adventures_of_tom_sawer = adventures_of_tom_sawer.replace("\n"," ")
print(adventures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""

adventures_of_tom_sawer = ("""\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth.""" )
adventures_of_tom_sawer = adventures_of_tom_sawer.replace("\n"," ")
adventures_of_tom_sawer = adventures_of_tom_sawer.replace("...."," ")
print(adventures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

adventures_of_tom_sawer = ("""\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth.""" )
adventures_of_tom_sawer = adventures_of_tom_sawer.replace("\n"," ")
adventures_of_tom_sawer = adventures_of_tom_sawer.replace("...."," ")
for _ in range(10):
    if " " not in adventures_of_tom_sawer:
        break
    adventures_of_tom_sawer = adventures_of_tom_sawer.replace("  ", " ")
print(adventures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

count_h = 0
for letter in adventures_of_tom_sawer:
    if letter == "h":
        count_h += 1

print("Кількість літер 'h':", count_h)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

words = adventures_of_tom_sawer.split()
count_capital = 0

for word in words:
    if word[0].isupper():
        count_capital += 1

print("Слів з великої літери:", count_capital)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""


words = adventures_of_tom_sawer.split()
count = 0

for index, word in enumerate(words):
    if word == "Tom":
        count += 1
        if count == 2:
            print("Слово 'Tom' вдруге зустрічається на позиції:", index + 1)
            break

# task 07
""" Розділіть змінну adventures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adventures_of_tom_sawer_sentences
"""
adventures_of_tom_sawer_sentences = None

adventures_of_tom_sawer_sentences = adventures_of_tom_sawer.split(".")
for sentence in adventures_of_tom_sawer_sentences:
    if sentence.strip():
        print(sentence.strip()+".")

# task 08
""" Виведіть четверте речення з adventures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

print(adventures_of_tom_sawer_sentences [3].strip().lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

for sentence in adventures_of_tom_sawer_sentences:
    if sentence.strip().startswith("By the time"):
        print("Є речення, що починається з 'By the time':")
        print(sentence.strip() + ".")
        break
else:
    print("Жодне речення не починається з 'By the time'.")

# task 10
""" Виведіть кількість слів останнього речення з adventures_of_tom_sawer_sentences.
"""

for sentence in reversed(adventures_of_tom_sawer_sentences):
    if sentence.strip(): # Перевірка, що речення не порожнє
        last_sentence = sentence.strip()
        break
words_in_last_sentence = last_sentence.split()
print("Кількість слів в останньому реченні:", len(words_in_last_sentence))