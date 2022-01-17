import requests
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler
from telegram.update import Update
from telegram.ext.filters import Filters
import settings

updater = Updater(token=settings.TELEGRAM_TOKEN)

def start(update: Update, context: CallbackContext):
    update.message.reply_text('           Assalamu Aleykum!'
                              ' DMaker botining test variantiga hush kelibsiz!'
                              ' Bu botdan foydalanish uchun /search va so`rovingizni yozing.'
                              ' Misol uchun /search samuray')

def search(update: Update, context: CallbackContext):
    args = context.args
    if len(args) == 0:
        update.message\
            .reply_text('Enter ur request! like such: /search Dua Lipa')
    else:
        search_text = ' '.join(args)
        response = requests.get('https://en.wikipedia.org/w/api.php', {
            'action': 'opensearch',
            'search': search_text,
            'limit': 1,
            'namespace': 0,
            'format': 'json'
        })

    result = response.json()
    link = result[3]

    if len(link):
        update.message\
            .reply_text('There u go : ' + link[0])
    else:
        update.message\
            .reply_text('No info was found according to ur request')

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('search', search))
dispatcher.add_handler(MessageHandler(Filters.all, start))

updater.start_polling()
updater.idle()