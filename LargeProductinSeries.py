x = open('longseries.txt')
series = list()
for digit in x:
    for i in digit:
        if not i == '\n':
            series.append(i)
products = list()
for y in range(0, len(series)-12):
    product = 1
    for x in range(0,13):
        product = product * int(series[y+x])
    products.append(product)
        # print(series[x])
    # print(series[y], sep=' ', end='', flush=True)
print(max(products))
