#coding=utf-8

inputnum = int(input('Please input number of layer : '))

s = ' '
for x in range(inputnum,0,-1):
    if x == 0:
        print(s*(inputnum-x)+'*')
    else:
        plist = [*range(0,x*2,1)]
        print(s*(inputnum-x),end='')
        for z in plist:
            if z == 0:
                print('*',end='')
            elif z%2 == 0:
                print('*',end='')
            elif z == plist[-1]:
                print('')
            else:
                print(s,end='')
