import time
import os
import requests
from bs4 import BeautifulSoup
def __main__():
    print('——SCiPNET 终端 ——')
    print('请稍等 我们正在对程序进行初始化设置。')
    time.sleep(1)
    os.system('title SCiPNET')
    os.system('color 0a')
    os.system('cls')
    print('Connecting to the server...')
    os.system('ping scp-wiki-cn.wikidot.com -n 1')
    url = 'http://scp-wiki-cn.wikidot.com'
    strhtml = requests.get(url) 
    print('Connect over.')
    now = int(time.time())
    timeArray = time.localtime(now)
    timeArray = time.localtime(now)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print('Time:',otherStyleTime,'Please Login.')
    user = input('You UserName:')
    password = input('Password:')
    password = 0
    print('Welcome',user)
    while True:
        command = input('Server>>')
        if command == 'help':
            print('access (SCPNumber) \n shutdown \n mail \n')
        if command[:6] == 'access':
            os.system('Explorer' + command[6:])
        if command == 'shutdown':
            print('Please wait, shutting down...')
            time.sleep(2)
            print('Now you can safely shut down the computer.')
            os.system('pause')
        if command == 'mail':
            print('SKiPNET has no sponsors now.')
if __name__ == "__main__":
    __main__()