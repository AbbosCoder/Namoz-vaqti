from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardRemove,ParseMode ,ReplyKeyboardMarkup,KeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.inline_tugma import *
from loader import dp,bot
from .namoz import *
from utils.misc import subscription
from data.config import ADMINS
from data.kanal import get_channels
from keyboards.default.tugmalar import *
from .mbaza import *



@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message):
    user_id = message.from_user.id 
    first_name = message.from_user.first_name 
    username = message.from_user.username
    language_code = message.from_user.language_code
    new_user = add_user(user_id,first_name,username)
    #args = message.get_args()
    if new_user:
        for admin in ADMINS: await bot.send_message(admin,f"New user: \nName: <a href='t.me/{username}'>{first_name}</a>\nID: <code>{user_id}</code> ",parse_mode='html')
    
    CHANNELS = get_channels()
    s = 0  
    count = len(CHANNELS)
    kanal_obuna = InlineKeyboardMarkup(row_width=1)
    for channel in CHANNELS:
        status = await subscription.check(user_id=user_id,channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            s += 1
        else:
            invite_link = await channel.export_invite_link()
            kanal_obuna.add(InlineKeyboardButton(text=f'➕ {channel.title}',url=invite_link))
    if s != count:
        kanal_obuna.add(InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs"))
        await message.answer("<b>Iltimos, botdan foydalanish uchun quyidagi hamkor kanallarimizga obuna bo'ling</b>",parse_mode='html',reply_markup=kanal_obuna)
    else:
        text = f'<b>Assalomu alaykum {first_name} \nSizga qayerni namoz vaqlari kerak?</b>'
        await message.answer(text,reply_markup=city,parse_mode='html')  
        
@dp.message_handler(commands='yordam')
async def yordam_c(message: types.Message):
    await message.answer("<i>Savol va takliflar uchun admin:\n@Abbosbek_Turdaliyev</i>",parse_mode='Html')

@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    first_name = call.message.chat.first_name
    CHANNELS = get_channels()
    s = 0
    count = len(CHANNELS)
    kanal_obuna = InlineKeyboardMarkup(row_width=1)
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id,channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            s += 1
        else:
            invite_link = await channel.export_invite_link()
            kanal_obuna.add(InlineKeyboardButton(text=f'➕ {channel.title}',url=invite_link))
    if s != count:
        await call.answer("Hamkor kanallarimizga obuna bo'ling !!!",show_alert=True)
        await call.message.delete()
        kanal_obuna.add(InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs"))
        await call.message.answer("<b>Iltimos, botdan foydalanish uchun quyidagi hamkor kanallarimizga obuna bo'ling</b>",parse_mode='html',reply_markup=kanal_obuna)
        
    else:
        await call.message.delete()
        text = f'<b>Assalomu alaykum {first_name} \nSizga qayerni namoz vaqlari kerak?</b>'
        await call.message.answer(text,reply_markup=city,parse_mode='html')
    await call.answer()

@dp.callback_query_handler(text='back')
async def back(call: types.CallbackQuery):
    first_name = call.from_user.first_name
    text = f'<b>Assalomu alaykum {first_name} \nSizga qayerni namoz vaqlari kerak?</b>'
    await call.message.edit_text(text,reply_markup=city,parse_mode='html') 

@dp.callback_query_handler(text='update')
async def update_namoz(call: types.CallbackQuery):
    location = get_joylashuv(call.from_user.id)
    text = namoz_kun(location)
    await call.message.edit_text(text,reply_markup=update,parse_mode='html') 

@dp.callback_query_handler(text='delete')
async def deete_msg(call: types.CallbackQuery):
    await call.message.delete()
    text = f'<b>Assalomu alaykum {call.from_user.first_name} \nSizga qayerni namoz vaqlari kerak?</b>'
    await call.message.answer(text,reply_markup=city,parse_mode='html')     
#oxirgi qatorga yozilsin
@dp.callback_query_handler()
async def zona(call: types.CallbackQuery):
    location = call.data
    user_id = call.from_user.id
    print(location,user_id)
    update_location(user_id,location)
    await call.message.edit_text(namoz_kun(location),reply_markup=update)
