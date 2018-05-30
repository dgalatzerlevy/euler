words = ['and','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen',
         'fifteen','sixteen','seventeen','eighteen','nineteen',
         'twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety','hundred','thousand']

longcount = 0

#count one thousand
def thousand():
    count = len(words[1]+words[-1])
    return count



#count the hundreds
def hundreds():
    count = len(words[-2])*900 #'hundred'
    count = count + len(words[0])*891 #'and'
    for i in range(1,10):
        count = count + len(words[i])*100 #numbers 1-9
    return count

def tens():
    count = 0
    for i in range(10,20):
        count = count + len(words[i])*10
    for i in range(20,28):
        count = count + len(words[i])*10
    return count

def ones():
    count = 0
    for i in range(1,10):
        count = count + len(words[i])*90
    return count

longcount = longcount + thousand() + hundreds() +tens()
print(longcount)

def makenumber(i):
    num = str(i)
    if i < 20:
        print(words[i])

for i in range(1,24):
    makenumber(i)