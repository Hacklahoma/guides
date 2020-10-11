import praw

## Enter the following information about your bot
USER_AGENT = ''
CLIENT_ID = ''
CLIENT_SECRET = ''
USERNAME = ''
PASSWORD = ''


## Creating a new bot instance 
bot = praw.Reddit(user_agent = USER_AGENT,
                  client_id = CLIENT_ID,
                  client_secret = CLIENT_SECRET,
                  username = USERNAME,
                  password = PASSWORD)

## This subreddit is useful
subreddit = bot.subreddit('testingground4bots')

## This maintains a constant stream of comments in real time
comments = subreddit.stream.comments()

## Looks at every 
for comment in comments: 
    text = comment.body ## Get comment's body
    author = comment.author ## Get comment's body
    if 'hackrice' in text.lower():
        ## Generate message
        message = "Hey u/{0}, it looks like you're interested in HackRice! For more information, please visit [our website](http://hack.rice.edu)".format(author)
        comment.reply(message) ## Send message