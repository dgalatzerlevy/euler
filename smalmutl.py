print('Starting...')
x = 1

for j in range(20,999999999999,20):
    for i in range(2,21):
        if not j%i == 0:
            print(j, 'failed at', i)
            break
        else:
            print(j, 'divides by', i)
            if i == 20:
                print(j)
                quit()
