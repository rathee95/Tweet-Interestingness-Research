import re
def getWords(text):
	for word in text.split():
		word1=re.sub('[^A-Za-z0-9]+', '', word)
		word2=re.sub('[^0-9]+', '', word1)
		if(word1!=word2):
			print (word1)
getWords(" hi b!' 12 http://www.gmail.com  abhi19 19 shrk 'adf'  ")
