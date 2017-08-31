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


bot = telebot.TeleBot(token)

welcome_message = '''Hello!
This bot is running on a heroku instance.'''

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, welcome_message)

print("Setting webhook url to: ", url)
bot.set_webhook(url + token)
