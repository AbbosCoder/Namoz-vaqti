from aiogram.dispatcher.filters.state import StatesGroup,State

class HisobRaqam(StatesGroup):
    phone_number = State()

class HisobRaqamru(StatesGroup):
    phone_number = State()

class InfoUser(StatesGroup):
    user_id = State()    

class SendADS(StatesGroup):
    ads = State()

class AddChannel(StatesGroup):
    channel_id = State()

class DelChannel(StatesGroup):
    channel_id = State()

class UserSendMsg(StatesGroup):
    user_id  = State()
    msg = State()    
     