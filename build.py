

def is_rotation(src, dest):

    if(src == dest):
        return True

    if src is None or dest is None:
        print 'None check'
        return False

    if len(src) != len(dest):
        print 'length'
        return False

    for x in range(0,len(src)):
        s = src[x+1:]+src[0:x+1]
        print s

        if s == dest:
            return True

    return False

print is_rotation('abcd' , 'cdab')
#print len('')
