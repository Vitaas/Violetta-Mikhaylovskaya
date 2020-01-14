def int_func(text):
    letter_old = text[0]
    letter_new = chr(ord(letter_old) - ord('a') + ord('A'))
    return letter_new + text[1:]


words = input().split()
text_list = []
for text in words:
    text_list.append(int_func(text))
print(' '.join(text_list))
