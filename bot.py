import telebot
import pymysql
import json
try:
    connection = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='',
        database='users',
        cursorclass=pymysql.cursors.DictCursor
    )

    print("successfully connected...")
    cursor = connection.cursor()
    print("#" * 20)

except Exception as ex:
    print("Connection refused...")
    print(ex)
bot = telebot.TeleBot("6570762751:AAEwozETUMOVUP81VK4FAZwwRcN6N86Aw_w", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    fn = message.from_user.first_name
    id = message.from_user.id
    get_users(message,fn,id)
    
    # print(message.from_user.first_name)
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)
    

def get_users(m,username, id):
    row = (username, id)
    cursor.execute("select * from users")
    exst = 'false'
    for string in cursor.fetchall():
          if string['chat_id']==id: exst = 'true'
          
    if exst=='false':
         query = "insert into users(name, chat_id) values(%s,%s)"
         cursor.execute(query, row)
         connection.commit()
         bot.reply_to(m, "Ваш id записан !")
    else:
        bot.reply_to(m, 'Ваш id уже в базе!')        
      
	  
    
     




bot.infinity_polling()