from aiogram import types
from aiogram.types import ParseMode
from aiogram.dispatcher import FSMContext
from loader import dp,bot
from data.config import ADMINS
from data.kanal import add_channel,del_channel,get_channels
from utils.misc import subscription
from .namoz import *
from keyboards.default.tugmalar import *
from keyboards.inline.inline_tugma import *
from handlers.users.mbaza import *
from states.asosiy import *
import time

@dp.message_handler(commands='admin',chat_id = ADMINS)
async def admin_start(message: types.Message, state: FSMContext):
    await message.answer(f'Assalomu alaykum {message.from_user.full_name}!\nADMIN PANEL:',reply_markup=admin_panel)

@dp.message_handler(text='Statistika 📈',chat_id = ADMINS)
async def statika(msg: types.Message):
    await msg.answer(f'Umumiy foydalanuvchilar: {users_count()} ta')

@dp.message_handler(text='Hisobot 📋',chat_id = ADMINS)
async def hisobot(msg: types.Message):
    file_name = export_data_to_excel()
    hisobot = open(file_name,'rb')
    await msg.answer_document(document=hisobot,caption="Barcha foydalanuchilarni ma'lumotlari exselga eksport qilindi!")

@dp.message_handler(text='Xabar yuborish ✉️',chat_id = ADMINS)
async def send_msg(message: types.Message):
    await message.answer("Xabar yuboring yoki biror joydan forward xabar yuboring... ",parse_mode='Html',reply_markup=cancel)
    await SendADS.ads.set()
@dp.message_handler(state=SendADS.ads,content_types=types.ContentTypes.ANY)
async def add_user_finish(message: types.Message, state: FSMContext):
    if message.text == '❌Bekor qilish':
        await message.answer("Xabar yuborish bekor qilindi!",reply_markup=admin_panel)
        await state.finish()
    else:    
        cursor.execute('SELECT id, first_name FROM users')
        users = cursor.fetchall()
        await message.answer('Xabar yuborish boshlandi...\nJarayon yakunlanmaguncha xabar yubormang\n<b>Biroz kuting...</b>',parse_mode='html')
        a,b=0,0
        for user_id, first_name in users:
            # Har bir foydalanuvchiga xabar yuborish
            try:
                await bot.copy_message(chat_id=user_id,
                                       from_chat_id=message.from_user.id,
                                       message_id=message.message_id,
                                       caption=message.caption,
                                       parse_mode=ParseMode.MARKDOWN,
                                       reply_markup=message.reply_markup)
                a+=1
                time.sleep(0.02)
            except Exception as e:
                #print(f"Xabar yuborishda xato yuz berdi: {e}")
                b+=1   
        await message.answer(f"✅ Xabar muvaffaqiyatli yuborildi!\n<b>Aktiv foydalanuvchilar: {a}\nBotni blocklaganlar: {b}\nYuborilgan xabarlar: {a+b}</b>",parse_mode='html' )
        await message.answer( '<b>ADMIN PANEL:</b>',
                             parse_mode=ParseMode.HTML,
                             reply_markup=admin_panel)
        await state.finish()           
@dp.message_handler(text='➕ Kanal qo\'shish',chat_id = ADMINS)
async def add_chanel(message: types.Message):
    await message.answer("Kanal IDisni kiriting: \nESLATMA BOT kanalda admin bo'lishi kerak!!!",parse_mode='Html',reply_markup=cancel)
    await AddChannel.channel_id.set()
@dp.message_handler(state=AddChannel.channel_id,content_types=types.ContentTypes.TEXT)
async def add_user_finish(message: types.Message, state: FSMContext):
    if message.text == '❌Bekor qilish':
        await message.answer("Kanal qo'shish bekor qilindi!",reply_markup=admin_panel)
        await state.finish()
    else:
        channel_id = message.text
        try:
            channel = await bot.get_chat(channel_id)
            await message.answer(f"Kanal: {channel.title} \nUsername: {channel.username} \nKanal qo'shildi",reply_markup=admin_panel)
            add_channel(channel_id=channel_id)
        except Exception as e:
            await message.answer(f"xatolik: {e}",reply_markup=admin_panel)
        await state.finish()
@dp.message_handler(text='➖ Kanal o\'chirish',chat_id = ADMINS)
async def send_msg(message: types.Message):
    await message.answer("Kanal IDisni kiriting: \nESLATMA BOT kanalda admin bo'lishi kerak!!!",parse_mode='Html',reply_markup=cancel)
    await DelChannel.channel_id.set()
@dp.message_handler(state=DelChannel.channel_id,content_types=types.ContentTypes.TEXT)
async def add_user_finish(message: types.Message, state: FSMContext):
    if message.text == '❌Bekor qilish':
        await message.answer("Kanal o'chirish bekor qilindi!",reply_markup=admin_panel)
        await state.finish()
    else:    
        channel_id = message.text
        del_channel(channel_id=channel_id)
        try:
            channel = await bot.get_chat(channel_id)
            await message.answer(f"Kanal: {channel.title} \nUsername: {channel.username} \nKanal o'chirildi",reply_markup=admin_panel)
        except Exception as e:
            await message.answer(f"xatolik: {e}",reply_markup=admin_panel)    
        await state.finish()
            
@dp.message_handler(text='Kanallar 📣', chat_id=ADMINS)
async def kanallar(msg: types.Message ):
    CHANNELS = get_channels()
    result = 'Kanallar ro\'yxati: \n'
    i=1
    for channel_id in CHANNELS:
        try:
            channel = await bot.get_chat(channel_id)
            result += f"{i}) {channel.title} \n@{channel.username} \n<code>{channel_id}</code>\n"
            i+=1
        except:
            result +=f"{i}) Bot kanalda admin emas: <code>{channel_id}</code>\n"
            i+=1
    await msg.answer(result)        
@dp.message_handler(text='Userga xabar yuborish 👤',chat_id = ADMINS)
async def send_msg(message: types.Message):
    await message.answer("Foydalanuvchi ID-sini kiriting:",reply_markup=cancel)
    await UserSendMsg.user_id.set()
    
# Get user ID handler
@dp.message_handler(state=UserSendMsg.user_id)
async def get_user_id(message: types.Message, state: FSMContext):
    if message.text == '❌Bekor qilish':
        await message.answer("Xabar yuborish bekor qilindi!",reply_markup=admin_panel)
        await state.finish()
    else:
        user_id = message.text
        await state.update_data(user_id=user_id)
        await UserSendMsg.next()
        await message.answer("Endi xabaringizni kiriting:")

# Get user message handler
@dp.message_handler(state=UserSendMsg.msg,content_types=types.ContentTypes.ANY)
async def get_user_message(message: types.Message, state: FSMContext):
    if message.text == '❌Bekor qilish':
        await message.answer("Xabar yuborish bekor qilindi!",reply_markup=admin_panel)
        await state.finish()
    else:
        user_data = await state.get_data()
        user_id = user_data.get("user_id")
          # Finish the state

        # Sending a message to the user with the provided ID
        try:
            await bot.copy_message(chat_id=user_id,
                                   from_chat_id=message.from_user.id,
                                   message_id=message.message_id,
                                   caption=message.caption,
                                   parse_mode=ParseMode.MARKDOWN,
                                   reply_markup=message.reply_markup)
            await message.answer("Xabar muvaffaqiyatli yuborildi!",reply_markup=admin_panel)
        except Exception as e:
            await message.answer(f"Xatolik yuz berdi: {e}",reply_markup=admin_panel)
        await state.finish()

@dp.message_handler(content_types=['text'])
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    link = message.text 
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
        kanal_obuna.add(InlineKeyboardButton(text="✅ Tekshirish ", callback_data="check_subs"))
        await message.answer("Iltimos, botdan foydalanish uchun quyidagi hamkor kanallarimizga obuna bo'ling",reply_markup=kanal_obuna)
    else:  
        matn = namoz_kun(link)
        text = 'Tanlang:'
        await message.answer(matn,reply_markup=update)

        
