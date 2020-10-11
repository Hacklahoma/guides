## Python libraries that we need to import for our bot
from flask import Flask, request
from pymessenger.bot import Bot ## pymessenger is a Python wrapper for the Facebook Messenger API

app = Flask(__name__) ## This is how we create an instance of the Flask class for our app

ACCESS_TOKEN = 'EAAak33Ya2S0BAPhkLa8X7TexIpuCisomkSZA3RqcCwZAYqfTo8rPGzWO0zZCZAZCpsUtSBkLkLXbtNrmm1y07tmZBhVsohjyZAZAbeLd1iomErwOgZAJB8WtZCjvyZBYZBSQZB5VlPULsu93ttsxBUyNEXnsOca3uD3IIOfM4ZA7EwsBYu0wZDZD'
VERIFY_TOKEN = 'TESTINGTOKEN' ## Replace 'VERIFY_TOKEN' with your verify token
bot = Bot(ACCESS_TOKEN) ## Create an instance of the bot

def verify_fb_token(token_sent):
    ## Verifies that the token sent by Facebook matches the token sent locally
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

# Chooses a message to send to the user
def get_message_text():
    return "Hey, it looks like you're interested in HackRice! For more information, please visit http://hack.rice.edu"

## Send text message to recipient
def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response) ## Sends the 'response' parameter to the user
    return "Message sent"

## This endpoint will receive messages 
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    print("MESSAGE RECEIVED")
    ## Handle GET requests
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token") ## Facebook requires a verify token when receiving messages
        return verify_fb_token(token_sent)

    ## Handle POST requests
    else: 
       output = request.get_json() ## get whatever message a user sent the bot
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                recipient_id = message['sender']['id'] ## Facebook Messenger ID for user so we know where to send response back to

                ## If user sends text
                if "hackrice" in message['message'].get('text').lower():
                    response_sent_text = get_message_text()
                    send_message(recipient_id, response_sent_text)

    return "Message Processed"

## Ensures that the below code is only evaluated when the file is executed, and ignored if the file is imported
if __name__ == "__main__": 
    app.run() ## Runs application