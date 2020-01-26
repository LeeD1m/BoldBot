import telebot

bot = telebot.TeleBot('1072089743:AAH9uL3pvC-8qWgcNd0lvDr3yz_JhslnNLY')
# keyboard1 = telebot.types.ReplyKeyboardMarkup()
# keyboard1.row('Привет', 'Пока')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Начнем, сучки')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'а' or message.text.lower() == 'а?':
        bot.send_message(message.chat.id, 'Хуй на')
    elif 'что' in message.text.lower():
        bot.send_message(message.chat.id, 'Хуй во что')
    elif 'че' in message.text.lower():
        bot.send_message(message.chat.id, 'Хуй во че')
    elif 'узк' in message.text.lower():
        bot.send_message(message.chat.id, 'Где мой конь, Татарка??')
    elif 'бот' in message.text.lower():
        bot.send_message(message.chat.id, 'Ди, не манди')
    elif message.text.lower() == 'ди':
        bot.send_message(message.chat.id, 'Ди, не манди')
    elif message.text.lower() == 'м' or message.text.lower() == 'м?':
        bot.send_message(message.chat.id, 'Йо, включи мозги!')
    elif message.text.lower() == 'смешно':
        bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAM9Xi3mlzMg82jj0Fem8LxmMVUYmxQAAqcDAALpCsgDb6SvkfCJUFIYBA')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()