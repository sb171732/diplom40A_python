import telebot

bot = telebot.TeleBot("6570762751:AAEwozETUMOVUP81VK4FAZwwRcN6N86Aw_w", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()