import os

import telebot
from loguru import logger
from telebot import apihelper, types

from constants import keyboards
from utils.io import write_json
import emoji


class Bot:
	def __init__(self):
		"""
		Template Telegram Bot.
		"""
		self.bot = telebot.TeleBot(os.environ["strangerbot_TOKEN"])
		self.echo_all = self.bot.message_handler(func=lambda message: True)(self.echo_all)

	def run(self):
		logger.info('Bot is runnig...')
		self.bot.infinity_polling()

	def echo_all(message):
		#write_json(message.json, 'message.json')
		self.bot.send_message(message.chat.id, message, message.text, reply_markup=keyboards.main)



if __name__ == '__main__':
	logger.info('Bot started')
	bot = Bot()
	bot.run()
