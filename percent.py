f = open('birds.txt', 'r', encoding = 'UTF-8')
s = f.readlines()
f.close()
k = []
for line in s:
    words = line.split(' ')
    for word in words:
        word = word.strip(',.<>?/\'":;#№!~\n\t[]{}*+-_()1234567890=')
        if word != '':
            k.append(word)
large = 0
h = 'П'
for el in k:
    if el.startswith(h):
        large += 1
    else:
        continue
prc = str((large/len(k))*100)
print(prc + '%')

