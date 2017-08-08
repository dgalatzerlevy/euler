
def isPalindrome(x):
    x = str(x)
    reverse = x[::-1]
    if x == reverse:
        return True
    else:
        return False

# x = input('Give me a palindrom:')
# print(isPalindrome(x))

xmin = int(input('min ',))
xmax = int(input('max ',)) + 1




products = list()

import itertools

for x, y in itertools.product(range(xmin,xmax),range(xmin,xmax)):
    products.append((x,y,x*y))

for product in products:
    if isPalindrome(product[-1]) == True:
        print(product)
