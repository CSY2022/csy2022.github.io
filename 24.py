def calc(num1,num2,sym1):
    result = 0
    if sym1 == 0:
        result = num1 + num2
    elif sym1 == 1:
        result = num1 - num2
    elif sym1 == 2:
        result = num1 * num2
    elif sym1 == 3 and num2 != 0:
        result = num1 / num2 
    elif sym1 == 4:
        result = num2 - num1
    elif sym1 == 5 and num1 != 0:
        result = num2 / num1
    return result      
i = 0
num = [0, 0, 0, 0]
for i5 in range(0,4):
    num[i5]=int(input('输入第'+str(i5+1)+'个数字'))
sym = [' + ', ' - ', '×', '÷',' - ','÷']
num_sum = 10
num_time = 24
for i1 in range(0, 4):
    num1 = num[i1]
    for i2 in range(0, 3):
        num2t = (i1 + i2 + 1) % 4
        num2 = num[num2t]
        y = num_sum  -  i1  -  2  -  num2t
        x = (num_time / (i1 + 1)) / (num2t+1)
        delta = (y*y - 4*x)**0.5
        for k1 in range(0,6):
            result1 = calc(num1,num2,k1)
            for i3 in range(0, 2):
                num3 = num[int((delta * ((-1) ** (i3 + 1)) + y) / 2)-1]
                num4 = num[int((delta  * ((-1) ** i3) + y) / 2)-1]
                for k2 in range(0,6):
                    result2 = calc(result1,num3,k2)  
                    for k3 in range(0,6):
                        result3 = calc(result2,num4,k3)
                        if result3 < 24.0001 and result3 > 23.9999:
                            i=i+1
                            print('第',i,'组解:')
                            if k1==5 or k1==4:
                                print(num2,sym[k1],num1,'=',"{:.2f}".format(result1))
                            else:
                                print(num1,sym[k1],num2,'=',"{:.2f}".format(result1))
                            if k2==5 or k2==4:
                                print(num3,sym[k2],"{:.2f}".format(result1),'=',"{:.2f}".format(result2))
                            else:
                                print("{:.2f}".format(result1),sym[k2],num3,'=',"{:.2f}".format(result2))
                            if k3==5 or k3==4:
                                print(num4,sym[k3],"{:.2f}".format(result2),'=',24)
                            else:
                                print("{:.2f}".format(result2),sym[k3],num4,'=',24)
                            print('')
if i == 0:
    print("无实数解")