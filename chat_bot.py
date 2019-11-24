#Setting up Chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#Train the bot
chatbot = ChatBot('Training Example')
trainer = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.english"
)

#Setting telegram things
tg_token='1069397471:AAGmk6G7aaFjeaUXFB-fKbPNUMHikTDsvp8' # Refer README for more details
import logging
from telegram.ext import CommandHandler,MessageHandler, Filters,Updater
updater = Updater(token=tg_token)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a chat bot")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()

def reply(bot, update):
    userText=update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=str(trainer.get_response(input())))

reply_handler = MessageHandler(Filters.text, reply)
dispatcher.add_handler(reply_handler)
