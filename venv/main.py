import requests as requests

url  = "https://api.telegram.org/bot1011533725:AAEITWgE26LelFvBjnV-TkWfEUKCIPwDx9w/"

def get_chat_id(update):
    chat_id = update['message']["chat"]["id"]
    return chat_id

def get_username(update):
    username = update['message']["chat"]["first_name"]
    return username

def get_message_text(update):
    message_text = update["message"]["text"]
    return message_text

def last_update(req):
    response = requests.get(req + "getUpdates")
    response = response.json()
    result = response["result"]
    total_update = len(result)-1
    return result[int(total_update)]

def size_messages(req):
    response = requests.get(req + "getUpdates")
    response = response.json()
    result = response["result"]
    total_update = len(result) - 1
    return int(total_update)

def send_message(chat_id,message_text):
    params = {"chat_id":chat_id,"text":message_text}
    response =requests.post(url + "sendMessage",data=params)

def main():
    update_id = last_update(url)["update_id"]
    while True :
        update = last_update(url)
        if update_id == update["update_id"]:
           if get_message_text(update).lower() == "salom" :
              send_message(get_chat_id(update), get_username(update) +  " Nichiksan bi " )
              update_id = update_id + 1
           if get_message_text(update).lower()=="/start":
              send_message(get_chat_id(update),get_username(update) + " Maishiy texnika olamiga xush kelibsiz...")
              update_id = update_id + 1

main()