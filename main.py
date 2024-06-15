import asyncio
import logging
import os
import re

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


# TEXT
@dp.message()
async def echo_handler(message: Message):
    gramms = re.findall('([0-9.]{1,5})г', message.text)
    calories, protein, fat, carbs = (re.findall(f'([0-9.]{{1,5}}){char}', message.text) for char in ['К', 'Б', 'Ж', 'У'])
    
    print(gramms)
    print(calories)
    print(protein)
    result_text = f'''{message.text}\n
    Вывод:
    {round(sum([float(x) * float(y) * 0.01 for x, y in zip(gramms, calories)]), 2)} кал
    {round(sum([float(x) * float(y) * 0.01 for x, y in zip(gramms, protein)]), 2)} белков
    {round(sum([float(x) * float(y) * 0.01 for x, y in zip(gramms, fat)]), 2)} жиров
    {round(sum([float(x) * float(y) * 0.01 for x, y in zip(gramms, carbs)]), 2)} углеводов
    '''

    await message.answer(result_text)


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
    if int(os.environ.get('DEBUG')):
        try:
            asyncio.run(main())
        except Exception as ex:
            logging.error(ex)
    else:
        while True:
            try:
                asyncio.run(main())
            except Exception as ex:
                logging.error(ex)