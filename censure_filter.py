banned_words = ['blin', 'Voldemort', 'Tom Riddle']
text = input("Enter text: ")

# fast and greedy solution
output_text = text
for banned_word in banned_words:
    output_text = output_text.replace(banned_word, "*" * len(banned_word))
print("Result: " + output_text)


# comparing with lower string
output_text = text
output_text_lower = output_text.casefold()
for banned_word in banned_words:
    banned_word_len = len(banned_word)
    banned_word = banned_word.casefold()
    try:
        while True:
            index = output_text_lower.index(banned_word)
            output_text_lower = "".join(
                (output_text_lower[:index], "*" * banned_word_len, output_text_lower[index + banned_word_len:]))
            output_text = "".join(
                (output_text[:index], "*" * banned_word_len, output_text[index + banned_word_len:]))
    except ValueError:
        pass
print("Result: " + output_text)


# use regular expression library (BEST SOLUTION) RegExp
import re
output_text = text
for bw in banned_words:
    pattern = re.compile(bw, re.IGNORECASE)
    output_text = pattern.sub("*" * len(bw), output_text)
print("Result: " + output_text)

