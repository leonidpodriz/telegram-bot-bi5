import telebot

bot = telebot.TeleBot("5079927509:AAEkR6Jje_tDskQk9Ml-rr9EddEt7CNO_rc")


@bot.message_handler(commands=['start'])
def greet_user(message):
    return bot.reply_to(message, 'Hello!')


bot.polling()
