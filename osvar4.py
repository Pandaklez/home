import re
import os

def kll4():
    d = {}
    imax = 0
    for root, dirs, files in os.walk('.'):
        if dirs != []:
            for dr in dirs:
                m = re.search('(.).+', dr)
                if m != None:
                    z = m.group(1)
                    if z not in d:
                        d[z] = 1
                    else:
                        d[z] += 1
                    if imax < d[z]:
                        imax = d[z]
    print(imax)
    print(d)        

def main():
    kll4()

if __name__ == '__main__':
    main()
