import tweepy
import configparser
import os

# Read consumer keys and access tokens from file, used for OAuth
config = configparser.ConfigParser()
config.read('authorization.ini')

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(config['Twitter']['consumer_key'], config['Twitter']['consumer_secret'])
auth.set_access_token(config['Twitter']['access_token'], config['Twitter']['access_token_secret'])

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

def tweet_meme(img_id, title=''):
  """
  Tweets an image given an id and title
  """

  img_path = get_img_path(img_id)
  try:
    api.update_with_media(img_path, status=title)
  except:
    print('! Something went wrong, the file path is probably invalid !')
    pass

print(api.me().name)
