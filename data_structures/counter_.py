from collections import Counter


print(issubclass(Counter, dict))

# letters = "ala ma kota i wszy"

# letter_counter = Counter(letters)
# print(letter_counter)

# podaj 10 najczęściej występujących słów powyżej 5 znaków w Panu Tadeuszu

# url = 'https://wolnelektury.pl/media/book/txt/pan-tadeusz.txt'
#
# import requests
#
# tadeusz = requests.get(url)
#
# # print(tadeusz.text)
# tadeusz_words = tadeusz.text.split(" ")
#
# validated_tadeusz_words = []
#
# for word in tadeusz_words:
#     if len(word) > 5:
#         validated_tadeusz_words.append(word)
#
#
# tadeusz_counter = Counter(validated_tadeusz_words)
#
# print(tadeusz_counter)

# from urllib.request import urlopen
# import re
#
# with urlopen("https://wolnelektury.pl/media/book/txt/pan-tadeusz.txt") as response:
#     text = response.read().decode('utf-8')
#     text = [word for word in re.findall(r'\b\w+\b', text) if len(word) > 5]
#     counter = Counter(text)
#     print(counter.most_common(10))


letters = ["a", "b", "c", "a", "c", "a", "b", "c"]

letter_counter = Counter(letters)
print(letter_counter)

letter_counter.update("aa")
letter_counter.update(["c", "c"])
letter_counter = Counter(letters)
letter_counter.update({"b": 3})
letter_counter.update(a=2, b=2, c=2)
print(letter_counter)

letter_counter.subtract(a=7, b=6, c=8)
print(letter_counter)

letter_counter.clear()
print(letter_counter)



# ====


c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)

print(c1 + c2)
print(c1 - c2)

print(c1 & c2)
print(c1 | c2)

print(+c1)  # chcemy tylko dodatnie
print(-Counter(a=1, b=-2))

print(list(c1.elements()))
print(c1.most_common())
print(c1.total())

