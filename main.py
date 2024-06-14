import asyncio
import logging
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command

from util import intro_menu_keyboard, insert_data_keyboard


load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.environ.get('TELEGRAM_TOKEN'))

dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('Hello', reply_markup=intro_menu_keyboard())


# CALLBACKS
@dp.callback_query(lambda call: str(call.data) == 'insert_data_menu')
async def insert_data_menu_start(callback: CallbackQuery):
    await callback.message.edit_text('Insert Data menu', reply_markup=insert_data_keyboard())


@dp.callback_query(lambda call: str(call.data) == 'to_intro_menu')
async def insert_data_menu_start(callback: CallbackQuery):
    await callback.message.edit_text('Hello', reply_markup=intro_menu_keyboard())


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())