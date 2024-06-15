# Из предложенного текстового файла (text18-32.txt) вывести на экран его содержимое,
# количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно вставив после каждой
# строки строку из символов «*».

with open("pz-11/text18-32.txt", 'r', encoding='utf-16') as f:
    text = f.read()
    print(text)
    text1 =''.join(text.split('\n')[:4])
    print(len(''.join([i for i in text1 if i in ",.?!"])))

with open("pz-11/text18-32new.txt", 'w', encoding='utf-16') as f:
    f.write("*\n".join(text.split("\n")) + '*')