import sys
import readline
from steer_fun import STEER_FUN
steer_fun = STEER_FUN()
speed = input("请输入移动速度:")
try:
    speed = float(speed)
except ValueError:
    print("请重开软件")
    
 
while True:
    temp = input("控制机械臂位号:")
    try:
        temp = int(temp)
    except ValueError:
        print("请重试")
        continue
    if(temp == 0):
        for i in range(1,7):
            if(i == 1):
                str_info = steer_fun.steer_get_val_1()
            elif(i == 2):
                str_info = steer_fun.steer_get_val_2()
            elif(i == 3):
                str_info = steer_fun.steer_get_val_3()
            elif(i == 4):
                str_info = steer_fun.steer_get_val_4()
            elif(i == 5):
                str_info = steer_fun.steer_get_val_5()
            elif(i == 6):
                str_info = steer_fun.steer_get_val_6()
            print(str(i)+"的当前值:"+str(str_info))

    elif(temp == 1):
        str_info = steer_fun.steer_get_val_1()
    elif(temp == 2):
        str_info = steer_fun.steer_get_val_2()
    elif(temp == 3):
        str_info = steer_fun.steer_get_val_3()
    elif(temp == 4):
        str_info = steer_fun.steer_get_val_4()
    elif(temp == 5):
        str_info = steer_fun.steer_get_val_5()
    elif(temp == 6):
        str_info = steer_fun.steer_get_val_6()
    print(str(temp)+"的当前值:"+str(str_info))
    val = input("请输入设定值:")
    try:
        val = int(val)
    except ValueError:
        print("请重试")
        continue
    if(temp == 1):
        steer_fun.steer_set_val_1(val,speed)
    elif(temp == 2):
        steer_fun.steer_set_val_2(val,speed)
    elif(temp == 3):
        steer_fun.steer_set_val_3(val,speed)
    elif(temp == 4):
        steer_fun.steer_set_val_4(val,speed)
    elif(temp == 5):
        steer_fun.steer_set_val_5(val,speed)
    elif(temp == 6):
        steer_fun.steer_set_val_6(val,speed)
    print(str(temp)+"号以达目标值"+str(val))






