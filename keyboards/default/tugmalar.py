from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

cancel = ReplyKeyboardMarkup(resize_keyboard=True,
                                   keyboard=[
                                      [KeyboardButton('❌Bekor qilish')]])

get_number = ReplyKeyboardMarkup(resize_keyboard=True,
                                   keyboard=[
                                      [KeyboardButton('📞 Telfon raqamni yuborish 📞',request_contact=True)],
                                      [KeyboardButton('❌cancel')]])

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True,
                                  keyboard=[
                                     [KeyboardButton("Statistika 📈"),[KeyboardButton('Kanallar 📣')]],
                                     [KeyboardButton("Hisobot 📋"),KeyboardButton("Xabar yuborish ✉️")],
                                     [KeyboardButton("➕ Kanal qo\'shish"),KeyboardButton("➖ Kanal o\'chirish")],
                                     [KeyboardButton('Userga xabar yuborish 👤')]
                                  ])   
keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                     keyboard=[
                                        [KeyboardButton('🚀 Pul ishlash'), KeyboardButton('📹 Video qo\'llanma')],
                                        [KeyboardButton('🏆 Top 30'),KeyboardButton('⚙️ Hisobni sozlash')],
                                        [KeyboardButton('💳 Mening hisobim')],
                                        [KeyboardButton('💰 Pul to’lanishiga isbotlar')]
                                     ])
  