import re
import os

def fhh():
    dic = {}
    imax = 0
    dirmax = ''
    for root, dirs, files in os.walk('E://Anni Docs//ВЫШКА//python'):
        m = re.search('(.*//)*(.+)', root)
        root = m.group(2)
        print(root)
        dic[root] = len(files)
        if imax < dic[root]:
            imax = dic[root]
            dirmax = root
    print(dic)
    print(dirmax + ' файлов максимум =' + str(imax))
            
def main():
    fhh()

if __name__ == '__main__':
    main()
