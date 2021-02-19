from bs4 import BeautifulSoup
import os
import time
import json
import requests
import pandas as pd
SAVEPATH = os.getcwd() + "\\result.json"
CSVPATH = os.getcwd() + "\\result.csv"
# lotteryCrawler
class KRLotteryCrawler:
	def __init__(self):
		self.lottoURL = "https://dhlottery.co.kr/gameResult.do?method=byWin"
	def crawlNum(self):
		req = requests.get(self.lottoURL)
		html = req.text
		soup = BeautifulSoup(html, 'html.parser')
		soup.find_all("div", class_="num win")
		rNum = []
		#print(nums)
		for idx in range(6):
			num = soup.select('.ball_645')[idx].get_text()
			rNum.append(num)
		#find bonus
		bonus = soup.find("div", class_="num bonus").select('.ball_645')[0].get_text()
		rNum.append(bonus)
		print(rNum)

	def crawlGameNum(self,game):
		data = {'drwNo': game }
		req = requests.post(self.lottoURL, params=data)
		html = req.text
		soup = BeautifulSoup(html, 'html.parser')
		soup.find_all("div", class_="num win")

		nums = []
		bns = []
		#print(nums)
		for idx in range(6):
			num = soup.select('.ball_645')[idx].get_text()
			#print(num)
			nums.append(num)
		#find bonus
		bonus = soup.find("div", class_="num bonus").select('.ball_645')[0].get_text()
		bns.append(bonus)
		rNum = {"회차":game,"ball1":nums[0],"ball2":nums[1],"ball3":nums[2],"ball4":nums[3],"ball5":nums[4],"ball6":nums[5],"bns":bns[0]}
		print(rNum)
		return rNum

	def getLastGameNum(self):
		req = requests.get(self.lottoURL)
		html = req.text
		soup = BeautifulSoup(html, 'html.parser')
		soup = BeautifulSoup(html, 'html.parser')
		res = soup.find(title="회차 선택").find(selected="").get_text()
		return res
	
	def crawlAllGames(self):
		games =[]
		for i in range(1,(int)(self.getLastGameNum())+1):
		#for i in range(1,10):
			nums = self.crawlGameNum(i)
			#print("회차["+ (str)(i) +"]:")
			print(nums)
			games.append(self.crawlGameNum(i))
		return games

	def saveAsFile(self, path=SAVEPATH):
		with open(path, "w+") as f:
			games = self.crawlAllGames()
			json.dump(games,f,indent=4)
			data = pd.DataFrame(games)
			data.to_csv(CSVPATH, index=False)
		f.close()

	def getFileLen(self,path=SAVEPATH):
		line=0
		with open(path, "r") as f:
			data = json.load(f)
			line = len(data)
		f.close()
		return line

	def isNeedUpdateLastGame(self):
		if(self.getFileLen()-1 == self.getLastGameNum):
			return True
		return False


a = KRLotteryCrawler()
a.saveAsFile()
# length = a.getFileLen()
# weblen = a.getLastGameNum()
# print(length)
# print(weblen)
#res = a.crawlGameNum(948)
#a.crawlAllGames()