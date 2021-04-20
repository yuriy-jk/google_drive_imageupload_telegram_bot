import telebot
import config
from google_drive_upload import drive_upload

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
        name = message.photo[-1].file_unique_id
        file_info = bot.get_file(file_id=id)
        print(file_info)
        downloaded_file = bot.download_file(file_info.file_path)
        drive_upload(downloaded_file, name)
        upload_message_text = 'Фото успешно загружено на Google Drive'
        bot.send_message(message.chat.id, upload_message_text)


if __name__ == '__main__':
    bot.infinity_polling()

