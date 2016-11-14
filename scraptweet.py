import tweepy 
import csv

consumer_key = "28JS************************q6GDavr"
consumer_secret = "kos**********************************kaVR6KyC9dfejVRqSQqYLipRMN6nZaoYwCKw4EG"
access_key = "44149913-Y**13c67tT8ID*********************OB3MDCU6"
access_secret = "yzKFo3uHim1fzR0eW4udIuYiTD2yH****************************8BN"

def get_all_tweets(screen_name):
	#initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []		
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	print(len(new_tweets))
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	count = 4
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0 and count > 0 :
		# print ("getting tweets before %s" % (oldest))
		count = count - 1 
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		#save most recent tweets
		alltweets.extend(new_tweets)
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		print ("...%s so far" % (len(alltweets)))
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"), tweet.retweet_count ,tweet.retweeted,tweet.user.favourites_count,tweet.user.friends_count] for tweet in alltweets]
	# write the csv	
	
	with open('%s.csv'%user, 'a') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text", "retweet_count", "tweet.retweeted" , "favourites_count" , "friends_count"])
		writer.writerows(outtweets)
	pass

	count = 1 
	alltweets_dict =[]
	new_tweets_dict = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
	alltweets_dict.extend(new_tweets)
	if alltweets_dict[-1].id:
		oldest_dict = alltweets_dict[-1].id - 1

	while len(new_tweets_dict) > 0 and count >0 :
		# print ("getting tweets before %s" % (oldest))
		count = count - 1 
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets_dict = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest_dict)
		#save most recent tweets
		alltweets_dict.extend(new_tweets)
		#update the id of the oldest tweet less one
		oldest = alltweets_dict[-1].id - 1
		print ("...%s so far" % (len(alltweets_dict)))
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets_dict = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"), tweet.retweet_count ,tweet.retweeted,tweet.user.favourites_count,tweet.user.friends_count] for tweet in alltweets_dict]

	with open('%sdictionary.csv'%user, 'a') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text", "retweet_count", "tweet.retweeted" , "favourites_count" , "friends_count"])
		writer.writerows(outtweets_dict)
	pass


	with open("%s.csv"%user, "r") as infile, open("%sC.csv"%user, "w") as outfile:
		reader = csv.reader(infile)
		writer = csv.writer(outfile)
		for row in reader:
			writer.writerow(item.replace(",", "") for item in row)
    
	with open("%sdictionary.csv"%user, "r") as infile, open("%sdictionaryC.csv"%user, "w") as outfile:
		reader = csv.reader(infile)
		writer = csv.writer(outfile)
		for row in reader:
			writer.writerow(item.replace(",", "") for item in row)
		for row in reader:
			writer.writerow(item.replace("b'", "") for item in row)	


if __name__ == '__main__':
	with open('users.csv', 'r') as f:
		reader = csv.reader(f)
		users = []
		for row in reader:
			users.append(row[0])
		for user in users:
			get_all_tweets(user)


	
