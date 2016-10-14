# Toa Mema 0.3.1
This is a Python 3 script that is used to moderate the [/r/BionicleMemes](http://www.reddit.com/r/bioniclememes) subreddit.

It is currently running on a VPS and is in development.

## Some features
* Counts the number of "meme" posts in the subreddit
* Alerts users via comment when they forget to flair their posts
* Updates the sidebar with information such as the days since Bionicle was cancelled
* Translate English to Matoran

#### Features on hold
* Tweet top posts to Twitter

#### Possible upcoming features
* Allow users to get special user flair not generally available
* Tally posts/karma per user to create a leaderboards
* Allow mobile users to flair via commenting
* Temporarily remove unflaired posts
* Super secret cool subreddit events!

## Setup and Configuration
Run this command to get the base requirements:

    pip install -r requirements.txt
Run this command to start the script:

    python toamema.py

### OAuth2
This script uses [OAuth2Util](https://github.com/SmBe19/praw-OAuth2Util/tree/master/OAuth2Util) to handle OAuth2.

You must include your own `oauth.ini` file for this script to run properly, check the README for OAuth2Util to find out what information you need to provide and how to get it.

### Twitter and Imgur
For this script to post on Twitter and upload to Imgur, you must provide a `authorization.ini` file in this format:

    [Twitter]
    consumer_key =
    consumer_secret =
    access_token =
    access_token_secret =

    [Imgur]
    client_id =
    client_secret =

### Matoran
You must provide your own `Matoran.ttf` font file for the bot to reference. The bot will only work in subreddits it is whitelisted to (default is None), you can set the whitelist in 'whitelist.txt' by writing the name of each subreddit on their own separate line.

To have Toa Mema translate an English sentence into Matoran, simple write a comment in the following format:

    /u/ToaMema [INSERT_MESSAGE]

#### Misc. Obvious Things
This bot is tailored specifically for /r/BionicleMemes and therefore is a pretty bad option for pretty much any other subreddit. ToaMema has redundant features offered by AutoModerator for the sake of consolidating bot actions. If you want to use ToaMema, you can, but you will need to make some (trivial) changes to the code and the final product will probably be suboptimal. I am primarily documenting this project for fun, however, if you would like to contribute, feel free to submit a pull request.
