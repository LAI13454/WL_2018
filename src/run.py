import json
class RUN:
    def __init__(self):
        f = open("config.json",encoding='utf-8')
        setting = json.load(f)
        print(setting)
    def gray_dif(self,gray):
        left = 0
        right = 0
        l1 = list(range(12))
        del l1[-1]
        print(l1)
        for i in l1:
            if((not gray[i]) and (gray[i+1])):
                print(i+1)
                left = i+1
                break
        l2 = list(gray)
        l2.reverse()
        for i in l1:
            if((not l2[i]) and (l2[i+1])):
                print(i+1)
                right = i+1
                break
        print(left - right)
    def turn_pid(self,dif):
        pass
run = RUN()
run.gray_dif((0,0,0,0,0,1,1,0,0,0,0,0))
        



