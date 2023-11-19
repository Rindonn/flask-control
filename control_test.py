'''
@ Author: Rindon
@ Date: 2023-11-08 16:04:57
LastEditors: Rindon
LastEditTime: 2023-11-18 13:45:07
@ Description: test remote control

'''
import requests
import time
def control_Test():
    '''
        description:'Test function for server',
        param:'control order input from keyboard',
        return:''
    '''
    control = input()
    #input ip address
    ip_Address = "192.168.137.38"
    port = '8000'
    path = '/server/'
    url = 'http://' + ip_Address + ':' + port + path

    url = url + control

    response = requests.get(url)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Wrong! Error code: {response.status_code}")

if __name__ == "__main__":
    while True:
        control_Test()


