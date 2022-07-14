import telebot
import requests


AUTH_TOKEN = '5194697271:AAF3v-E8E9dCdXi1gtqZQWwKcRYwbNeFIdQ'

bot = telebot.TeleBot(AUTH_TOKEN)

def main():
    bot.polling()

@bot.message_handler(commands = ['submit'])
def greet(message):

    chatid = message.chat.id

    print(message.chat.id)
    rawtext = message.text
    rawtext = rawtext.split()[1]
    print(rawtext)

    dictionary = {
        "var":rawtext
    }
    
    check = requests.post("http://localhost:5000/submit", json=dictionary)
    
    
    if check.text == "phishing":
        msg = "PHISHING"
    else:
        msg = "LEGITIMATE"
    # bot.send_message(chatid, msg)
    bot.reply_to(message, msg)

if __name__ == '__main__':
    main()
