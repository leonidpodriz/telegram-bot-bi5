import telebot

from sevices import greet_name

bot = telebot.TeleBot("5079927509:AAEkR6Jje_tDskQk9Ml-rr9EddEt7CNO_rc")


@bot.message_handler(commands=['start'])
def greet_user(message):
    bot.reply_to(message, greet_name(message.chat.first_name))


@bot.message_handler(commands=['convert'])
def convert_currency(message):
    words = message.text.split()

    if len(words) != 3:
        bot.reply_to(message, 'Не могу понять твой запрос...')
    else:
        currency = words[1]
        amount = words[2]

        if not amount.isnumeric():
            bot.reply_to(message, f'Сумма должна быть в числах, а у тебя: {amount}')
        else:
            bot.reply_to(
                message,
                f"Похоже, ты хочешь конвертировать {amount} с {currency} в гривну..."
            )


bot.polling()
