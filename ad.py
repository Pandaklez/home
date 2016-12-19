import re
import os

def openfile(name1, name2):
    f = open(name1, 'r', encoding = 'utf-8')
    st = f.readlines()
    f.close()
    f = open(name2, 'r', encoding = 'utf-8')
    sh = f.read()
    f.close()
    #clean = cleantext(sh)
    #print(sh)
    wg = []
    for line in st:
        line = line.strip('\r\n')
        wg.append(line)
    wl = set(wg)
    wh = sh.split(' ')
    wh = set(wh)
    wordl = wl & wh
    print(wordl)
    f = open('wordlist.txt', 'w', encoding = 'utf-8')
    wrdl = list(wordl)
    wrdl = '\n'.join(wrdl)
    f.write(wrdl)
    f.close()
    return wg

def mstm(wg):
    #print(wg)
    os.system('C:\\Users\\student\\Desktop\\mystem -nid C:\\Users\\student\\Desktop\\adyghe.txt C:\\Users\\student\\Desktop\\rus_nouns.txt')
    f = open('C:\\Users\\student\\Desktop\\rus_nouns.txt', 'r', encoding = 'UTF-8')
    s = f.read()
    f.close()
    m = re.findall()

def main():
    mstm(openfile('adyghe.txt', 'news.html'))

if __name__ == '__main__':
    main()
    
