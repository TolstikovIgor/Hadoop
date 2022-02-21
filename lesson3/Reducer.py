#!/usr/bin/env python
"""reduser.py"""

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# читаем строки из STDIN
for line in sys.stdin:
    line = line.strip()
    # line = line.lower()
    # удаляем пробелы в конце и начале строки
    # разделяем пары ключ и значение
    try:
        word, count = line.split('\t', 1)
    except Exception:
        continue
    # преобразуем значение в число
    try:
        count = int(count)
    except ValueError:
        # игнорируем ошибки
        continue

    # на Reduce приходят данные после фазы Sort
    # поэтому этот код будет работать
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # пишем результат в STDOUT
            print(current_word+'\t'+current_count)
        current_count = count
        current_word = word
    # не забываем про последнее слово
if current_word == word:
    print(current_word+'\t'+current_count)