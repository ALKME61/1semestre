# Из заданной строки отобразить только символы пунктуации. Использовать
# библиотеку string.
# Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"

import string

line = '--msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"'

cs = [c for c in line if c in string.punctuation]

print(cs)
