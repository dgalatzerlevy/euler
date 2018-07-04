from string import ascii_uppercase as albet



file = open('names.txt','r')

names = list()

namestr = file.read().replace('"','')

namelist = namestr.split(',')
namelist.sort()
total = 0

for i in range(len(namelist)):
    name = namelist[i]
    namenum = i + 1
    nameval = 0
    for letter in name:
        nameval = nameval + albet.index(letter) + 1
##    print(i+1,name, nameval)
    total = total + nameval*(i+1)

print(total)



    

