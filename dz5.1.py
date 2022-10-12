# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

line = 'Напишите программу абвгдейку, удаляющую из текста все слова, содержащие ""абв"".'
print(f"Исходный текст: {line}")
words = line.split(' ')
fragment = 'абв'
new_words = []
for word in words:
    if fragment not in word:
        new_words.append(word)
new_words = ' '.join(new_words)
print(f"Исправленный текст: {new_words}")