import praw
import json
out_filename = 'keywordSubredditResearch.txt'

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='',
                     username='',
                     password='s')

redditor = reddit.redditor("leanluis").saved(limit=None)
with open(out_filename, 'w') as out_file:
    
    for saved in redditor:
        print(saved.subreddit)
        out_file.write(str(saved.subreddit) + '\n')
    
    
    