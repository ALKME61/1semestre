# currentSymbol = 'C'
# b = ord(currentSymbol)

# print(chr(b-1), chr(b+1))

##########################################

def del_num(text):
    rtrn = ''
    for i in text:
        if not i.isdigit():
            rtrn += i
    return rtrn

a = 'abcdefghijkl123mnopqr32stuvwxyz'
c = del_num(a)
b = []
isAlphabetic = True

for i in range(0, len(c) - 1):
  if ord(c[i]) + 1 == ord(c[i+1]):
    b.append(ord(c[i]))
    continue
  else:
    isAlphabetic = False
    print('Не по порядку', c[i] ,ord(c[i+1]), c[i+1])
    break

if isAlphabetic != False:
  print('0')
