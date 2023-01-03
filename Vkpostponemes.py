import vk_api as api
import time
import sys

file = open('config.txt', 'r')
TOKEN = file.read()
session = api.VkApi(token=TOKEN)
vk = session.get_api()




shorts = []
sh = input('Enter short name(id)')
while sh != "STOP":
    shorts.append(sh)
    sh = input('Keep on enterinf ids. Enter "STOP" to stop')
names = vk.users.get(user_ids = shorts, name_case = 'dat')
ids = [] # массив c id указанных людей
for i in range(len(shorts)):
    ids.append(names[i]['id'])
print(ids)
text = input('Enter message text')
first = []
last = []
for i in range(len(ids)):
    first.append(names[i]['first_name'])
    last.append(names[i]['last_name'])

day = int(input('Enter date'))
month = int(input('Enter month'))
year = int(input('Enter year'))
hour = int(input('Enter hour'))
minute = int(input('Enter minute'))

print("Are you thure that you want to send", text, "to", last, 'at', str(hour)+':'+str(minute), str(day)+'.'+str(month)+'.'+str(year))
conf = input('(y/n)?')
if conf == 'y':
    while True:
        struct = time.localtime()
        y = struct.tm_year
        m = struct.tm_mon
        d = struct.tm_mday
        h = struct.tm_hour
        minu = struct.tm_min
        print('Waiting...')
        if year <= y and month <= m and day <= d and hour <= h and minute <= minu:
            for i in range(len(ids)):
                vk.messages.send(user_id=ids[i], random_id=0, message=text)
            print("Messange was sent.")
            break
        time.sleep(10)
else:
    sys.exit()
