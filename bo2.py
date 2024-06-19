import telebot
from pytube import YouTube
bot = telebot.TeleBot("7365596714:AAHOWrgvBj0QkrXm0_Oy1ukaHzxKOhiqzpc")
@bot.message_handler(commands=['start'])
def message(message):
    bot.send_message(message.chat.id,'Hello im a bot for downloading videos from Youtube, please send a youtube video link and i will send you downloaded video.')
@bot.message_handler(func=lambda message: True)
def url(message):
    if message.text.startswith('https://www.youtube.com/'):
        try:
            yt = YouTube(message.text)
            stream = yt.streams.get_highest_resolution()
            stream.download()
            bot.send_chat_action(message.chat.id, 'upload_video')
            bot.send_video(message.chat.id, open(f"{yt.title}.mp4", 'rb'))
        except Exception as e:
            bot.reply_to(message, f"There is an error: {e}")
    else:
        bot.reply_to(message, "Please send a valid url.")
bot.polling()