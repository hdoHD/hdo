import requests 
import telebot 
from telebot import types
import requests
from uuid import uuid4
import random
import os
import json
from user_agent import generate_user_agent
import sys
from datetime import datetime
from bs4 import BeautifulSoup
import datetime

id = "1491448291"
tok = "7108009780:AAHjU1o9xwqxCv-odiqmkPH3J5vJjbG0MEs"

zzk=0
bot = telebot.TeleBot(tok)
@bot.message_handler(commands=['start'])
def start(message):
 global zzk
 zzk+=1
 nm = message.from_user.first_name
 id2 = message.from_user.id
 userk = message.from_user.username
 zxu = datetime.datetime.now()
 tt=f'''
عضو يستخدم البوت…
ـــــــــــــــــــــــــــــــــــــــ
اسم المستخدم : {nm}
يوزر المستخدم : @{userk}
ايدي المستخدم : {id2}
رقم المستخدم  : {zzk}
الوقت : {zxu}
ـــــــــــــــــــــــــــــــــــــــ
ـ @P_W_7'''

 key = types.InlineKeyboardMarkup()
 bot.send_message(id, f"<strong>{tt}</strong>",parse_mode="html",reply_markup=key);zin = types.InlineKeyboardButton(text ="تعـديل صـوره", callback_data = 'zn')
 fr = message.from_user.first_name
 maac = types.InlineKeyboardMarkup()
 maac.row_width=2
 maac.add(zin)
 bot.send_message(message.chat.id,f"<strong>اهلا بك : | {fr} في بـوت تـعديل الصـور للحصول على معلوماتك [ /info ]</strong>",parse_mode="html",reply_markup=maac)
@bot.callback_query_handler(func=lambda call:True)
def st(call):

 if call.data =="zn":
  nc1 = types.InlineKeyboardMarkup(row_width=2)
  MC = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='ارسل الصوره المطلوب تعديلها',reply_markup=nc1)
  bot.register_next_step_handler(MC,z1)
  

def z1(message):
    key = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, f"<strong>يتـم اجـراء تعـديل اصبـر قليلاً مـن فضـلك </strong>",parse_mode="html",reply_markup=key)
    iiid = str(message.from_user.id)
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)	
    with open(f"image{iiid}.jpg", 'wb') as new_file:
    	new_file.write(downloaded_file)    	
    Imge = requests.post("https://api2.pixelcut.app/image/upscale/v1", files = {'image': open(f'image{iiid}.jpg', 'rb')}, data = {'scale': '2'})
    with open(f"image{iiid}New.jpg", 'wb') as new_file:
    	new_file.write(Imge.content)
    send=open(f'image{iiid}New.jpg', 'rb')
    
    file = {'document':send}
    requests.post(f'https://api.telegram.org/bot{tok}/sendDocument?chat_id={message.chat.id}&caption=تـم تعـديل بـواسـطه : @P_W_7', files=file)
    
    #bot.send_photo(iiid,file=send,caption="تـم تعـديل بـواسـطه : @P_W_7")
    #print(Imge.text)
    os.system(f'rm -rf image{iiid}.jpg')
    os.system(f'rm -rf image{iiid}New.jpg')
	
bot.polling(none_stop=True)

