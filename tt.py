f = open('f.txt', 'r', encoding = 'UTF-8')
s1 = f.readlines()
f = open('g.txt', 'r', encoding = 'UTF-8')
s2 = f.readlines()
k = []
for line in s1:
    words = line.split(' ')
    for word in words:
        word = word.lower()
        word = word.strip(',.<>?/\'":;#№!~\n\t[]{}*+-_()1234567890=')
        if word != '':
            k.append(word)
kk = []
for line in s2:
    words = line.split(' ')
    for word in words:
        word = word.lower()
        word = word.strip(',.<>?/\'":;#№!~\n\t[]{}*+-_()1234567890=')
        if word != '':
            kk.append(word)

kkm = set(kk)
km = set(k)
res = kkm & km
print(res)
