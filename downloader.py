import sys, os, re
import praw, urllib


def dupeCheck(file_name, file_path):
	file_list = os.listdir(file_path)
	file_exists = file_name in file_list
	return file_exists

#def isAlbum(file_name):
#	return re.match('\..+', file_name) == None


if len(sys.argv) < 4:
	print('Not enough arguments: \n' +
		'Need number of images, download directory, and subreddit name')
	sys.exit()

script, image_num, file_path, subreddit = sys.argv

reddit_conn = praw.Reddit(user_agent='Reddit Image Downloader 1.0 by Ed Tirado')
submissions = reddit_conn.get_subreddit(subreddit).get_hot(limit = int(image_num))

for title in submissions:
	link  = title.url
	file_name = link.split('/')[-1]

	if dupeCheck(file_name, file_path):
		continue
	
	print('Downloading ' + file_name)
	urllib.request.urlretrieve(link,file_path + '/' + file_name)


