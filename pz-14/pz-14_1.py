# Из исходного текстового файла (experience.txt) выбрать стаж работы. Посчитать
# количество полученных элементов. 

import re 

filename = 'pz-14/experience.txt' 

with open(filename, 'r', encoding='utf-8') as file:
    content = file.read() 

pattern = re.compile(r'(\d+ (год(а|ов)?|лет))(\s+\d+ месяц(а|ев)?)?') 

matches = pattern.findall(content) 

count = len(matches) 

print("Найденные стажи работы:")
for match in matches: 
    print(match[0] + (f' {match[3]}' if match[3] else ''))
print(f"\nКоличество найденных элементов: {count}")