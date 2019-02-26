import tweepy 
import re
import codecs
import urllib2

ckey = ''
csecret = ''
atoken = ''
asecret = ''
list_hashtag = []
new_list_hashtag = []
count = 0

def internet_on():
	try:
		response=urllib2.urlopen('https://www.google.co.in',timeout=20)
		return True
	except urllib2.URLError as err: pass
	return False


auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
api = tweepy.API(auth)


quotes = open('Quotes.txt','r')
quotes = quotes.readlines()
quotes[count] = quotes[count].decode('ascii','ignore')


hashtag_trends = api.trends_place("1")

for i in range(len(hashtag_trends[0]['trends'])):
	list_hashtag.append(hashtag_trends[0]['trends'][i]['name'])

for j in range(len(list_hashtag)):
	if list_hashtag[j][0] == '#':
		new_list_hashtag.append(list_hashtag[j])

for k in range(len(new_list_hashtag)):
	if len(new_list_hashtag[k]) < 18 :
		hashtag = new_list_hashtag[k]
		break

tweet_len = len(quotes[count])+len(hashtag)+len(" #Quotes")

if internet_on() == True:
	if tweet_len <= 140:
		api.update_status(status = quotes[count] + hashtag + ' #Quotes')
		quotes = quotes[count+2:]
	else:
		quotes = quotes[count+2:]

	quotelist = open('Quotes.txt','w')
	quotelist = open('Quotes.txt','a')
	for items in quotes:
		quotelist.write("%s"% items)
