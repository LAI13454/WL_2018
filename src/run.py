import json
class RUN:
	def __init__(self):
		self.dif_last = 0
		f = open("config.json",encoding='utf-8')
		setting = json.load(f)
		self.KP = setting["PID_turn"]["P"]
		self.KI = setting["PID_turn"]["I"]
		self.KD = setting["PID_turn"]["D"]
		print("PID:",self.KP,self.KI,self.KD)
	def gray_dif(self,gray):
		left = 0
		right = 0
		l1 = list(range(12))
		del l1[-1]
		#print(l1)
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
		return(left - right)
	def turn_pid(self,dif):
		out = self.KP * dif + self.KD * (dif - self.dif_last)
		self.dif_last = dif
		return out
        
