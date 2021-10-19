from webdav3.client import Client
import os
import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

options ={
 'webdav_hostname': '',
 'webdav_login':    '',
 'webdav_password': ''
}

try:
    print('active')
except WebDavException as e:
    print(e)




text = "Actions:\n1) Upload file\n2) Info\n3) Make Directory\n4) Check existence of the resource\n5) Download Resource\n6) Help\nEnter here: "

action = str(input(text))

str = False
if str == True:
    print('Please input a number instead of a string of text!')
else:

    if action == "1":
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
        client = Client(options)
        client.verify = True
        infodir = input('file directory (example: hello/Dog): ')
        info = client.info(infodir)
        print(info)

    if action == '3':
        dirname = input('Directory name: ')
        dirpath = input('Directory Path: ')
        client = Client(options)
        client.verify = True
        client.execute_request('mkdir', "/" + dirpath + '/' + dirname)

    if action == '4':
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
        client = Client(options)
        client.verify = True
        dir = input('file directory: ')
        downloadahh = input('What file would you like to download?\nplease remember the .filetype (example: dog.gif): ')
        name = downloadahh.split('.')[0]
        filetype = downloadahh.split('.')[1]
        print(filetype)
        result = client.check('new/d' + name + '.' + filetype)
        if result == True:
            print('File already exists!')
        else:
            print('Check 1: Success!')
            e = os.listdir('./new')
            if downloadahh in e:
                print("Couldn't continue!")
            else:
                f = open('d~' + name + '.' + filetype, 'wb')
                f.close()
                client.download_sync(remote_path=dir + '/' + downloadahh, local_path='new/d' + name + '.' + filetype)
                print('new/d~' + name + '.' + filetype)
