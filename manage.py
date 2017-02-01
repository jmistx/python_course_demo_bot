import os
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = os.environ.get('TOKEN', 'TOKEN')
PORT = os.environ.get('PORT', 'PORT')


def echo(bot, update):
  update.message.reply_text('Bot answer: ' + update.message.text)

updater = Updater(TOKEN)
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.setWebhook('https://calm-crag-96590.herokuapp.com/{0}'.format(TOKEN))
updater.idle()
