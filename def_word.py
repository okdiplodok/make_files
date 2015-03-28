def def_collect(fname):
    y = codecs.open(fname, 'r', 'utf-8')
    g = codecs.open(u'definition.txt', 'r', 'utf-8')
    for line in y:
        line = line.split(u';')
        for line1 in g:
            if line1.startswith(line[0]):
                yield line1
            
        
    

for element in def_collect(u'rare.txt'):
    print element
            
