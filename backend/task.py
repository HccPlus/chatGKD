import time
import json
import os


def command():
    file = open("command", encoding="UTF-8")
    text = file.read()
    file.close()
    os.system(text)


def Sleep(data):
    sec = 0
    sec += 3600*data['hour']
    sec += 60*data['minute']
    sec += data['second']

    times = data['times']

    while True:
        command()
        if times and times > 0:
            times -= 1
            if times <= 0:
                break
        time.sleep(sec)


def Schedual(data):
    done = False
    while True:
        if data['year'] != None and time.localtime().tm_year != data['year']:
            done = False
            continue
        if data['month'] != None and time.localtime().tm_mon != data['month']:
            done = False
            continue
        if data['mday'] != None and time.localtime().tm_mday != data['mday']:
            done = False
            continue
        if data['hour'] != None and time.localtime().tm_hour != data['hour']:
            done = False
            continue
        if data['minute'] != None and time.localtime().tm_min != data['minute']:
            done = False
            continue
        if data['second'] != None and time.localtime().tm_sec != data['second']:
            done = False
            continue
        if not done:
            command()
            done = True


file = open("task.json", encoding="UTF-8")
JsonStr = file.read()
file.close()
JsonData = json.loads(JsonStr)

mode = JsonData['mode']

if mode == 'sleep':
    Sleep(JsonData['sleep'])
elif mode == 'schedual':
    Schedual(JsonData['schedual'])
else:
    print("Error")
