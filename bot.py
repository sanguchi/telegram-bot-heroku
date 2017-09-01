from os import environ
import telebot


print("Loading bot module")


if("TELEGRAM_TOKEN" in environ):
    token = environ["TELEGRAM_TOKEN"]
else:
    exit("Environment variable TELEGRAM_TOKEN not set, please add it using 'heroku config:set TELEGRAM_TOKEN=<TOKEN>'")


if("HEROKU_URL" in environ):
    url = environ["HEROKU_URL"]
    # Handle missing slash
    if(not url.endswith('/')):
        url = url + '/'
else:
    exit("Environment variable HEROKU_URL not set, please add it using 'heroku config:set HEROKU_URL=<URL>'")


welcome_message = '''Hello!
This bot is running on a heroku instance.
URL: {}'''.format(url)

# If you put the welcome message below this line you will make a big mistake:
# url actually is set to "etc.herokupp.com" but this line edits the url adding the 
# bot token, so you will leak your bot token if you move the welcome message.
url = url + token
bot = telebot.TeleBot(token)



@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, welcome_message)

print("Setting webhook url to: ", url)
bot.set_webhook(url)
