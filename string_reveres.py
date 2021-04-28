# input  -> "hello world"
# output -> "dlrow olleh"

phrase = input("Enter your phrase: ")


# solution 1
phrase_reversed = ""
for i in range(1, len(phrase) + 1):
    phrase_reversed += phrase[-i]  # phrase_reversed = phrase_reversed + phrase[-i]
print(f"Result 1: '{phrase_reversed}'")
print(f"Result 2: '{phrase[::-1]}'")


# solution 2
lst = list(phrase)
lst_half_len = int(len(lst) / 2)
for i in range(lst_half_len):
    temp = lst[i]
    lst[i] = lst[-(i + 1)]
    lst[-(i + 1)] = temp
print(f"Result 3: '{''.join(lst)}'")
