import json
import os
import pandas as pd
from collections import Counter
import numpy as np
import random

SAVEPATH = os.getcwd() + "\\result.json"
CSVPATH = os.getcwd() + "\\result.csv"
class AnalysisLottery :
	def __init__(self):
		print("LOG:Init AnalysisLottery")
		self.data=pd.read_csv(CSVPATH)

	def checkNumberRate(self):
		numList = list(self.data['ball1'])+list(self.data['ball2'])+list(self.data['ball3'])+list(self.data['ball4'])+list(self.data['ball5'])+list(self.data['ball6'])
		count = Counter(numList)
		most = count.most_common()
		print(most)

# 당첨번호를 원핫인코딩벡터(ohbin)으로 변환
def numbers2ohbin(numbers):
	ohbin = np.zeros(45) #45개의 빈 칸을 만듬
	print(numbers[1])
	for i in range(6): #여섯개의 당첨번호에 대해서 반복함
		ohbin[int(numbers[i])-1] = 1 #로또번호가 1부터 시작하지만 벡터의 인덱스 시작은 0부터 시작하므로 1을 뺌
	return ohbin

# 원핫인코딩벡터(ohbin)를 번호로 변환
def ohbin2numbers(ohbin):
	numbers = []
	for i in range(len(ohbin)):
		if ohbin[i] == 1.0: # 1.0으로 설정되어 있으면 해당 번호를 반환값에 추가한다.
			numbers.append(i+1)
	return numbers

a = AnalysisLottery()
#a.checkNumberRate()
#li = [9,22,32,23,29,41,39,35,28,6,25,42,16,24,2]
#for i in range(5):
	# sampleList = random.sample(li, 6)
	# print(sampleList)

df2 = a.data.iloc[:,1:7]
#print(df2[0,])
#ohbins = list(map(numbers2ohbin, df2))
#print(ohbins)
