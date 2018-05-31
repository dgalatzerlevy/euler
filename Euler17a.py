words = ['and','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen',
         'fifteen','sixteen','seventeen','eighteen','nineteen',
         'twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety','hundred','thousand']

longcount = 0

#count one thousand
def thousand():
    count = len(words[1]+words[-1])
    print(words[1]+words[-1]+"x1")
    return count



#count the hundreds
def hundreds():
    count = len(words[-2])* 900 #'hundred'
    print(words[-2]+"x900")
    count = count + len(words[0])*891 #'and'
    print(words[0]+"x891")
    for i in range(1,10):
        count = count + len(words[i])*100 #numbers 1-9
        print(words[i]+'x100')
    return count

def tens():
    count = 0
    for i in range(10,20):
        count = count + len(words[i])*10
        print(words[i]+'x10')
    for i in range(20,28):
        count = count + len(words[i])*100
        print(words[i]+'x100')
    return count

def ones():
    count = 0
    for i in range(1,10):
        count = count + len(words[i])*90
        print(words[i]+'x90')
    return count

longcount = longcount + thousand() + hundreds() +tens() +ones()
print(longcount)