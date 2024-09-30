from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
# '-1001856326427','-1001974484440','-1001833925242','-1001913358589','-1001819627505'
#CHANNELS = [ '-1001856326427','-1001974484440' ]
