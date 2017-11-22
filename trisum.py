##
##Let us list the factors of the first seven triangle numbers:
##
## 1: 1
## 3: 1,3
## 6: 1,2,3,6
##10: 1,2,5,10
##15: 1,3,5,15
##21: 1,3,7,21
##28: 1,2,4,7,14,28
##We can see that 28 is the first triangle number to have over five divisors.
##
##What is the value of the first triangle number to have over five hundred divisors?

#x = int(input('how high? '))


def tri(x):
    nums = list(range(x+1))
    trinum = sum(nums)
    return trinum

def divisors(x):
    div = list()
    for i in range(2,x+1):
        if x%i == 0:
            div.append(i)
    #print(div)
    return len(div)


largest = (0,0)
i = 0#17907118 #last big one I had
#for i in range(1,x+1):
while largest[1] < 500:
    i = i + 1
    current = divisors(tri(i))
    print('.', sep='', end='', flush=True)
    #print(i,current)
    if current > largest[1]:
        largest = (tri(i),current)
        print(largest)


print(largest)
