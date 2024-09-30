from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

check_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Obunani tekshirish", callback_data="check_subs")
        ]
    ]
)



city = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton('Toshkent',callback_data='Toshkent'),InlineKeyboardButton('Andijon',callback_data='Andijon')],
        [InlineKeyboardButton('Namangan',callback_data='Namangan'),InlineKeyboardButton('Jizzax',callback_data='Jizzax')],
        [InlineKeyboardButton('Buxoro',callback_data='Buxoro'),InlineKeyboardButton('Navoiy',callback_data='Navoiy')],
        [InlineKeyboardButton('Farg\'ona',callback_data='Farg\'ona'),InlineKeyboardButton('Sirdaryo',callback_data='Sirdaryo')],
        [InlineKeyboardButton('Samarqand',callback_data='Samarqand'),InlineKeyboardButton('Qarshi',callback_data='Qarshi')],
        [InlineKeyboardButton('Xiva',callback_data='Xiva'),InlineKeyboardButton('Shahrixon',callback_data='Shahrihon')]

    ]
)

update = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="♻️",callback_data='update'),InlineKeyboardButton('❌',callback_data='delete')
        ],
        [
            InlineKeyboardButton('🔙 orqaga',callback_data='back')
        ]
    ]
)