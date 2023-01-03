import vk_api as api
import time

file = open('config.txt', 'r')
TOKEN = file.read()
session = api.VkApi(token=TOKEN)
vk = session.get_api()

day = int(input('Введите дату'))
month = int(input('Введите month'))
year = int(input('Введите year'))
hour = int(input('Введите hour'))
minute = int(input('Enter minute'))


shorts = []
sh = input()
while sh != "STOP":
    shorts.append(sh)
    sh = input()
print(shorts)
names = vk.users.get(user_ids = shorts)
ids = [] # массив c id указанных людей
for i in range(len(shorts)):
    ids.append(names[i]['id'])
print(ids)
text = input('Введите текст сообщения')
while True:
    struct = time.localtime()
    y = struct.tm_year
    m = struct.tm_mon
    d = struct.tm_mday
    h = struct.tm_hour
    minu = struct.tm_min
    print('Ожидание...')
    if year <= y and month <= m and day <= d and hour <= h and minute <= minu:
        for i in range(len(ids)):
            vk.messages.send(user_id=ids[i], random_id=0, message=text)
        print("Сообщение отправлено")
        break
    time.sleep(10)
