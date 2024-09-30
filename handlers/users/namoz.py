import requests
from datetime import datetime, timedelta

def time_now():
    # Joriy vaqt
    current_time_utc = datetime.utcnow()

    # UTC +5 soat qo'shib olamiz
    time_utc_plus5 = current_time_utc + timedelta(hours=5)

    # Soatni olish
    hours = time_utc_plus5.hour
    minutes = time_utc_plus5.minute
    seconds = time_utc_plus5.second

    # Vaqtni formatlash
    formatted_time = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    text= f"🔄 Yangilangan vaqti: <code>{formatted_time}</code>"
    return text



def namoz_kun(region):
    url = f'https://islomapi.uz/api/present/day?region={region}'
    response = requests.get(url)
    if response.status_code==200:
        response = response.json()
        date = response['date']
        weekday = response['weekday']
        hijriy_date = response['hijri_date']
        hijriy_oy=hijriy_date['month']
        times= response['times']
        text = f'''
📆Sana: <code>{date}</code> Kun: <code>{weekday}</code>
📆Hijriy: <b>{hijriy_oy.title()}</b>, <code>{hijriy_date['day']}</code>
➖➖➖➖➖➖➖➖➖➖
⏰ <code>{times['tong_saharlik']}</code> ⏰ Tong <b>Saharlik</b>     
⏰ <code>{times['quyosh']}</code> ⏰ Quyosh        
⏰ <code>{times['peshin']}</code> ⏰ Peshin        
⏰ <code>{times['asr']}</code> ⏰ Asr            
⏰ <code>{times['shom_iftor']}</code> ⏰ Shom <b>Iftorlik</b>          
⏰ <code>{times['hufton']}</code> ⏰ Xufton   
➖➖➖➖➖➖➖➖➖➖
{time_now()}'''     
        return text
    else:
        return False    


def namoz_hafta(region):
    url = f'https://islomapi.uz/api/present/week?region={region}'
    response = requests.get(url).json()[2]
    print(response)
    date = response['date']
    weekday = response['weekday']
    hijriy_date = response['hijri_date']
    times= response['times']
    print(date,weekday)
    print(hijriy_date,times)