banned_words = [
    'blin',
    'dodon',
]

text = input("Enter text: ")

for banned_word in banned_words:
    text = text.replace(banned_word, "*" * len(banned_word))
print(text)
