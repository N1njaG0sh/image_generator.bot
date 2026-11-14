import telebot
from config import TOKEN
from logic import generate_image

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я твой бот по генерации картинок. Напиши что хочешь сгенерировать и я отправлю тебе готовую картинку!))')

@bot.message_handler(content_types=['text'])
def create_image(message):
    promt = message.text
    generate_image(promt, image_path=f'photo_{message.chat.id}.jpg')
    with open(f'photo_{message.chat.id}.jpg', 'rb') as file:
        bot.send_photo(message.chat.id, file)




bot.polling()