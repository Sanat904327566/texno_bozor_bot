import telebot
import time
import requests as requests

url  = "https://api.telegram.org/bot1011533725:AAEITWgE26LelFvBjnV-TkWfEUKCIPwDx9w/"
bot_token = '1011533725:AAEITWgE26LelFvBjnV-TkWfEUKCIPwDx9w'
bot = telebot.TeleBot(bot_token)
pic = "http://d.adroll.com/r/ISRFVJ4CYZEJLCRYPCOWW4/XRVEJ4F2K5DF7C2C4OV7OI/1c856f90de364cdcacbf36f9d0efb0a7.re?adroll_ad_payload=__HIAmQBkwHFAlHIAk0AAW3RzWvTYBwH8CSdTjYdWGEHLyp4UZY0yZM0yfDSl3VvXTPHWF2RhSTN2uDy0jTd7EU2EYaoA_EiE0FkXoaHCc4_YHtk4p4niCB4GCJ6EE-CiIgwNAie9Pb7wvfw4ft7RzAdsFct54aHpyul0WymUhpR02N8IQMmkvBMPQz9Zn8q5bfDuufSTTOw_bDJmJ6TarSsZmh7booDgsIdh71grMBPlaaAOpHPZYfLAJwfyIyrMuwdyebBYHlcGJoYlEq5wfgeyqeL_RExAtvn4FFjTjcvaYZ3WfMD27TdWmEnSX3YfPR4eQ8t37zxau39-uvN-92jWxcjgtz_NUMasCc7UFTL2uTQgFZQi_n6VmvVatELMYjmDLQUfV5Z_IKuQSpooesw-S8ercDOsu1WvYUmWoWUmkH3ohnw8Qd68N_2QwKtZdBL2FnV9aohAbS7c7DjdkRQPQ5CMfbbk69vNj5d3Xh-6y8WYUignzs9iSV4yJq3q56rhbj_Ltq_wzIiJhOQNDCZhIc5WWS4NGB4iWExeQp2TVpm3fXmvFobk6chgUkbJkLfxNSFiDjxvRNT0_BIs-G3atq8pHGKBjBV2cbUzJ8xMeVE5NmnzzDViIjE2y5MXYGpmu44umY7fuD5VqCZuu9b1T6aYxmeFaQ-lhFEIAG5jwZMOi2LmFqE3QLDsSyQLZqN8wt4kheAqYiyopiCNStLsi6a7CynyIZo8UqatzC1G4_TdnXHjqnRHnHMplnJMHVDF2UJcLxgGiLuKG7jA-uwO7BCPahZYfzq38QMRlJnOKAWGXoKDvde&adroll_subnetwork=r&cpm=XjPj-AAOBUEKsohEAAkUmkNRgyyQez6HEfFRCA&adroll_network=g&clickurl=https://adclick.g.doubleclick.net/aclk%3Fsa%3DL%26ai%3DCuCQg-OMzXsGKOMSQygWaqaTgAfOx77BN7oarw03AjbcBEAEgAGDd5vYNggEXY2EtcHViLTYxNjYzMTY0NzQxOTQ1OTLIAQmoAwGqBLsBT9COzYN2Tdil0uAP0kPHyDKJvfaJqyJLgSZoo--FsKfqVXRy3OLMgRsAjlPSULu2EXwtGptAsLpt-Z9lQvJwdfN1buVcNqqqMMARyl3XoopDBmQUAI176StfYKlSEixvWFhGf87FrPYcIRlyPssBsD0cIG07QwfOFgOyICD7GbLMKuuPQQSSSHivaYKb656cgtlbFZFNUmPXSjmRvhQhQy5GzMjVSXc1tzYColf6ygffLu6aHMKxvejGs4AGiOCvlc2G6cUzoAYhqAemvhuoB_LZG6gH7NUb2AcA0ggFCIABEAE%26num%3D1%26sig%3DAOD64_3v3KJ7S9NadevInko9eNoZ-Oqq9Q%26client%3Dca-pub-6166316474194592%26adurl%3D.jpg"


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

bot.send_photo(chat_id=994669408, photo='https://telegram.org/img/t_logo.png')

def main():
    while True :
        update = last_update(url)
        update_id = last_update(url)["update_id"]
        if update_id == update["update_id"]:
           if get_message_text(update).lower() == "salom" :
               send_message(get_chat_id(update), get_username(update) + " Salom")
               update_id = update_id + 1
           if get_message_text(update).lower()=="/start":
              send_message(get_chat_id(update),get_username(update) + " Maishiy texnika olamiga xush kelibsiz...")
              update_id = update_id + 1
           if get_message_text(update).lower() == "rasm":
              bot.send_photo(get_chat_id(update),pic)


main()