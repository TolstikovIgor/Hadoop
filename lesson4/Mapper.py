#!/usr/bin/env python
"""mapper.py"""

import sys

for line in sys.stdin:
    # удаляем лишние пробелы
    line = line.strip()
    # делим строки на слова
    words = line.split(',')
    try:
        word = words[4]
        # price = words[5]
        # добавляем значение для счетчика
        # for word in words:
        # выводим в output пару ключ и значение
        print(word.lower()+'\t')
    except Exception:
        continue
