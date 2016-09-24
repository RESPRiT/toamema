import tweepy
import os
 
# Read consumer keys and access tokens from file, used for OAuth
f = open('twitter.txt', 'r')
consumer_key = f.readline().rstrip()
consumer_secret = f.readline().rstrip()
access_token = f.readline().rstrip()
access_token_secret = f.readline().rstrip()
f.close()
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

def get_img_path(img_id):
  for fname in os.listdir('images'):
    img_path = 'images\\' + fname
    if(os.path.isfile(img_path) and os.path.splitext(fname)[0] == img_id):
      return img_path
  
  return None

def tweet_meme(img_id, title=''):
  img_path = get_img_path(img_id)
  try:
    api.update_with_media(img_path, status=title)
  except:
    print('! Something went wrong, the file path is probably invalid !')
    pass