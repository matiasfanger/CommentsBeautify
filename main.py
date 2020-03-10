import sys
import re


def loadConfig(obtainList,file):
    
    f = open(file, 'r')
    content = f.readlines()

    if obtainList == True:
        realcontent = []
        for i in content:
            r = re.search('\n',i)
            if r != None or r == None:
                if r == None:
                    realcontent.append(i)
                if r != None:
                    j = re.sub('\n', '',i)
                    realcontent.append(j)

        return realcontent

def textShow(file):
    
    content = loadConfig(True,file)

    last = ''
    for i in content:
        if len(i) > len(last):
            last = i
        else:
            continue
    
    width = len(last)
    k=0

    with open(file, 'a+') as f:

        topbar = ('#' * (width+4))
        f.write("\n\n\n")
        f.write("%s\n" % topbar)
        secondbar = ('#' + ' ' * (width+2) + '#')
        f.write("%s\n" % secondbar)
        for i in content:
            inside = ('# ' + content[k] + ' ' *  (width-len(content[k])+1) + '#')
            f.write("%s\n" % inside)
            k=k+1
        lastbar = ('#' + ' ' * (width+2) + '#')
        f.write("%s\n" % lastbar)
        bottombar = ('#' * (width+4))
        f.write("%s\n" % bottombar)

        f.close()
        print('Done!')

textShow(str(sys.argv[1]))