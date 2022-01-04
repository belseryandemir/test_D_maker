from telegram import *
from telegram.ext import *
from requests import *

updater = Updater(token="5098782966:AAHGj39Ay3oWAIpGG1Ty5faJRUbteQwXdP4")
dispatcher = updater.dispatcher

someMusicOnPC = "browse on your pc"
someMusicOnInter = "search the music"

someMusicOnPCUrl = "https://audioalter.com/preset/8d-audio"
someMusicOnInterUrl = "https://www.shazam.com/ru"


def startCommand(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton(someMusicOnPC)], [KeyboardButton(someMusicOnInter)]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ur welcome",
                             reply_markup=ReplyKeyboardMarkup(buttons))


def messageHandler(update: Update, context: CallbackContext):
    if someMusicOnPC in update.message.text:
        music = get(someMusicOnPCUrl).content
    if someMusicOnInter in update.message.text:
        music = get(someMusicOnInterUrl).content

    if music:
        context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[InputMediaMusic
                                                                            (music, caption="")])


dispatcher.add_handler(CommandHandler("start", startCommand))
dispatcher.add_handler(MessageHandler(Filters.text, MessageHandler))

updater.start_webhook()