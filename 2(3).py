import vk_api
import time
import requests
from course import *

vk = vk_api.VkApi(token = 'vk1.a.UpINWoPZYx2HVzZPAYfhNoJQDY8NeIOr1X8wLGLKRMilijjaV_4-FNlstS5YBNZFFBPMxURpiRt8UuncU4Zt4gL0MTWrnSGB12PZd73mAQp9p2FM7z4-oEmZKOuGzn2UHO2CiWbZUBB-UbM63oir3Yhsmo0Mlc0K-Ild1Y8TSjg7LZzhI5R5nUp2I98bC3t2U48_wBK52_QiO_0NyjrBWg')

vk._auth_token() # авторизация токена


# message = vk.method("messages.getConversations",
#                     {
#                         'count':20,
#                         'filter':'unanswered'
#                     }
#                     )

# print(
#         message['items'][0]['last_message']
#     )


# id_l = message['items'][0]['last_message']['from_id']# id - пользователя
# message_id = message['items'][0]['last_message']['id']# id - сообщения

# vk.method(
#     "messages.send",
#     {
#         'peer_id':id_l,
#         'random_id': message_id,
#         'message':"Привет"
#     }
#     )

while True:
    #получаю сообщения
    message = vk.method("messages.getConversations",
                        {
                            'count':20,
                            'filter':'unanswered'
                        }
                        )
    if message['count'] >= 1:  #если сообщений больше 1
        print(message)
        id_l = message['items'][0]['last_message']['from_id']# id - пользователя
        message_id = message['items'][0]['last_message']['id']# id - сообщения
        message_text = message['items'][0]['last_message']['text']# текст сообщения
        #проверка текста сообщения пользователя
        if message_text.lower() == "привет":
            vk.method("messages.send",    #отправка сообщения
                        {
                            'peer_id':id_l,
                            'random_id': message_id,
                            'message':"Привет"
                        }
                    )
        elif message_text.lower() == 'Планеты':
            url = 'https://swapi.dev/api/'
            response = requests.get(url).json()
            planets_api = response.get('planets')
            def check_pl(url):
                diam = []
                for i in range(1, 11):
                    response = requests.get(f'{url}/{i}').json()
                    diam.append({response.get('diameter'): response.get('name')})
                    diam.sort('diameter')
                    print(diam[-1])

            vk.method('messages.send',
                      {
                            'peer_id':id_l,
                            'random_id': message_id,
                            'message':"Привет"
                      }
                      )
        elif message_text.lower() == 'курс':
            vk.method('messages.send', {'peer_id': id_l, 'random_id':message_id,'message':})
        else:
            vk.method("messages.send",
                        {
                            'peer_id':id_l,
                            'random_id': message_id,
                            'message':"Такой команды я не знаю"
                        }
                    )

time.sleep(1)


