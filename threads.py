import urllib.request as ur

#'http://ngisnrj.ru/news/121764/'

for number in range(10607, 144444):
    address = 'http://www.forumishqiptar.com/threads/' + str(number) + '/'
    try:
        page = ur.urlopen(address)
        text = page.read().decode('ISO-8859-1')
        print('PAGE EXISTS')
        
        m = re.search('<blockquote class=.+?>(.+?)</bl', text, flags = re.DOTALL)
        if m != None and m != []:
            d = m.group(1)
            print(d)
            
        try:
            filename = 'посты.txt'
            f = open(filename, 'a', encoding = 'ISO-8859-1')
            f.write(d)
            f.close()
        except:
            print('Error with making txt file occured')
            sys.exit(0)
            
    except:
        print('Page doesn\'t exist')
        continue
