from webdav3.client import Client
import os
import subprocess
from pprint import pprint
import pynput
from pynput import keyboard

options ={
 'webdav_hostname': '',
 'webdav_login':    '',
 'webdav_password': ''
}
while True:
    os.system('clear')
    run = True
    if run == True:
        client = Client(options)
        client.verify = True
        files1 = client.list()
        pprint(files1)
    text = """
    Actions:    1) Upload file    2) Info    3) Make Directory    4) Check existence of the resource    5) Download Resource\n    Enter here: """

    action = str(input(text))

    str = False
    if str == True:
        print('Please input a number instead of a string of text!')
    else:
        key = 'l'
        def on_press(key):
            client = Client(options)
            client.verify = True
            files1 = client.list()
            pprint(files1)
            print('---------------------------------------------------------------------------------------------------------------------------')
        if action == "1":
            print('Make directory activated -------------------------------------------  Remember, type dir in all inputs to see all home directories')
            client = Client(options)
            client.verify = True
            dir2 = input("what is the file you would like to upload: ")
            dir = input('dir name: ')
            result = client.check('/' + dir + '/' + dir2)
            if result == 'True':
                print('Error could not make file, it may already exist')
            else:
                client.upload_sync(remote_path='/' + dir + '/' + dir2, local_path="./" + dir2)

        if action == '2':
            print('metadata info -------------------------------------------------------  Remember, dir in all inputs to see all home directories')
            client = Client(options)
            client.verify = True
            infodir = input('file directory (example: hello/Dog): ')
            info = client.info(infodir)
            print(info)

        if action == '3':
            print(' make directory ------------------------------------------------------  Remember, dir in all inputs to see all home directories')
            dirname = input('Directory name: ')
            dirpath = input('Directory Path: ')
            client = Client(options)
            client.verify = True
            client.execute_request('mkdir', "/" + dirpath + '/' + dirname)

        if action == '4':
            print('Check if file already exists ------------------------------------ Remember, dir in all inputs to see all home directories')
            dircheck = input('What directory would you like to check a file in?: ')
            filecheck = input('What file would you like to check?: ')
            client = Client(options)
            client.verify = True
            result = client.check('/' + dircheck + '/' + filecheck)
            if result == True:
                print('File already exists!')
            else:
                print('File does not exist!')

        if action == '5':
            print('Download files from directories ---------------------------------- Remember, dir in all inputs to see all home directories')
            client = Client(options)
            client.verify = True
            dir = input('file directory: ')
            downloadahh = input('What file would you like to download?\nplease remember the .filetype (example: dog.gif): ')
            name = downloadahh.split('.')[0]
            filetype = downloadahh.split('.')[1]
            print(filetype)
            result = client.check('Downloads/d' + name + '.' + filetype)
            if result == True:
                print('File already exists!')
            else:
                print('Check 1: Success!')
                e = os.listdir('./Downloads')
                if downloadahh in e:
                    print("Couldn't continue!")
                else:
                    f = open('d~' + name + '.' + filetype, 'wb')
                    f.close()
                    client.download_sync(remote_path=dir + '/' + downloadahh, local_path='new/d' + name + '.' + filetype)
                    print('new/d~' + name + '.' + filetype)
