# -*- coding: cp1251 -*-
import os
import codecs

def files_create(fname, x, z):
    f = codecs.open(fname, 'r', 'utf-8')
    n = 0
    l = 1
    arr = []
    for line in f:
        if line.startswith(u'<h2'):
            n += 1
            final = n + x
            name_dirs = u'Part_' + str(final)
            if not os.path.exists(name_dirs):
                os.makedirs(name_dirs)
            arr.append(line)
        elif n == 0:
            arr.append(line)
        elif line.startswith(u'<div class="section"'):
            if arr[-2].startswith(u'<h2'):
                arr.append(line)
            else:
                name = str(l + z) + u'.txt'
                dirs = u'./' + name_dirs
                s = codecs.open(os.path.join(dirs, name), 'a', 'utf-8')
                for element in arr:
                    s.write(element)
                s.close()
                arr = []
                arr.append(line)
                l += 1
        else:
            arr.append(line)
    new_name = str(l + z) + u'.txt'
    m = codecs.open(os.path.join(dirs, new_name), 'a', 'utf-8')
    for element in arr:
        m.write(element)
    m.close()
    return l

first = files_create(u'fp.htm', 0, 0)
second = files_create(u'sp.htm', 4, first)

def annotation():
    count = 1
    if not os.path.exists(u'mystem'):
        os.makedirs(u'mystem')
    app = os.path.join(u'.', u'mystem.exe')
    for root, dirs, files in os.walk(u'.'):
        for fname in files:
            if fname.endswith(u'.txt'):
                new_name = u'mystem\\' + u'a' + str(count) + u'.txt'
                route = app + u' -cn ' + os.path.join(root, fname) + u' ' + os.path.join(root, new_name)
                print route
                os.system(route)
                count += 1

result = annotation()

