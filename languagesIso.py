import re

def openfile(name):
    it = []
    f = open(name, 'r', encoding = 'UTF-8')
    s = f.read()
    f.close()
    return s

#def language(openfile):
#    sv = openfile('Русскийязык.html')
#    itt = sv.split('\n')
#    for el in itt:
#        mm = re.search('возвращает код этого языка хз как', el)
#        if mm != None:
#            codd = mm.group(1)
#            print(codd)

def findiso(s):
    it = s.split('\n')
    dic = {}
    i = 0
    for el in it:
        m = re.search('<td>(.*)</td>', el)
        if m != None:
           gfh = m.group(1)
           i += 1
           if i == 4:
               iso = gfh
               dic[lang] = [iso]
               continue
           m = re.search('<a',gfh)
           if m != None:
                res = re.search('>(.*)</a>', gfh)
                if res != None:
                    i = 0
                    lang = res.group(1)
    for key in dic:
        st = str(dic[key])
        ss = str(key)
        ss = ss + '\t' + st + '\n'
        maketsv(ss)
      
def maketsv(ss):
    f = open('статьиоязыках.tsv', 'a', encoding = 'UTF-8')
    f.write(ss)
    f.close()

def main():
    findiso(openfile('Кодыязыков.html'))

if __name__ == '__main__':
    main() 
    
            
        
