import praw
from praw.models import Comment, Submission
import json
import os
import sys

reddit = praw.Reddit(client_id='-',
                     client_secret='',
                     user_agent='',
                     username='',
                     password='')

out_filename = 'test.txt'

with open(out_filename, 'w') as out_file:
    
    for item in reddit.user.me().saved(limit=None):
        out_file.write(item.id + '\n')
        submission = reddit.submission(id=item.id)
     
        out_file.write(submission.title + '\n')
    
    
    
        out_file.write(submission.title + '\n')
        out_file.write(submission.url + '\n')
        # or combine title and url on same line like this
        # out_file.write(submission.title + ': ' + submission.url + '\n') 