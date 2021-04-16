import telebot
import config

bot = telebot.TeleBot(config.token)
group_id = -1001265505003


@bot.message_handler(func=lambda message: True and message.chat.id == group_id,
                     content_types=['text', 'photo'])
def pictures_id(message):
    if message.content_type == 'text':
        text = message.text
        bot.send_message(message.chat.id, message.text)
        print(text)
    if message.content_type == 'photo':
        print(message.photo)
        id = message.photo[-1].file_id
        file = bot.get_file(file_id=id)
        print(file)
        link = 'https://api.telegram.org/file/bot' + config.token + '/' + file.file_path
        print(link)
        bot.download_file(file_path=link)


# @bot.message_handler(content_types=['text'])
# def repeat_message(message):
#     bot.send_message(message.chat.id, message.text)
#
#


if __name__ == '__main__':
    bot.infinity_polling()

