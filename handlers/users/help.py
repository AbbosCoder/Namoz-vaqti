from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp,Command
from .mbaza import *
from loader import dp

@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/yordam - Yordam")
    
    await message.answer("\n".join(text))


