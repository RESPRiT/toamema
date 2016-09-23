# Toa Mema 0.2
This is a Python3 script that is used to moderate the [/r/BionicleMemes](http://www.reddit.com/r/bioniclememes) subreddit.

It is currently running and is in development.

## Some features
* Counts the number of "meme" posts in the subreddit
* Alerts users via comment when they forget to flair their posts
* Updates the sidebar with information such as the days since Bionicle was cancelled

## Possible upcoming features
* Allow users to get special user flair not generally available
* Tally posts/karma per user to create a leaderboards
* Translate English to Matoran
* Post top posts to /r/BionicleLego (probably weekly, given permission)
* Tweet top posts to Twitter

## Basic usage
Run this command to get the base requirements:

    pip install -r requirements.txt
Run this command to start the script:

    python toamema.py

## OAuth2
This script uses [OAuth2Util](https://github.com/SmBe19/praw-OAuth2Util/tree/master/OAuth2Util) to handle OAuth2.

You must include your own `oauth.ini` file for this script to run properly, check the README for OAuth2Util to find out what information you need to provide and how to get it.