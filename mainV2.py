from webdav3.client import Client
import os
from pprint import pprint
from os import system
from time import sleep

options ={
 'webdav_hostname': '', #for example, http://123.21.0.1/directory (not a real IP, just random numbers)
 'webdav_login':    '', #just your WebDav username
 'webdav_password': '' #password for you WebDav server
}



print("""
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------""")


#selection to select an action
text = """ 
Actions:    1) Upload file    2) Info    3) Make Directory    4) Check existence of the resource    5) Download Resource\n6) Listdir -------- Enter here: """


#asks what action you want to activate
action = str(input(text))


#not nessasary but it was from something i was trying to do that failed, it works, so i left it in.
str = False
if str == True:
    print('Please input a number instead of a string of text!')
else:

    #make directory
    if action == "1":
        print('Make directory activated -------------------------------------------  Remember, "dir" in all inputs to see all home directories')
        run = True
        if run == True:
          #prints all files in assinged directory
            client = Client(options)
            client.verify = True
            files1 = client.list()
            pprint(files1)
            print('-----------------------------------------------------------------------------------------------------------------------------------')
        client = Client(options)
        client.verify = True
        dir2 = input("what is the file you would like to upload: ")
        dir = input('dir name: ')
        if dir == "dir":
            #prints directory
            files1 = client.list()
            pprint(files1)
        else:
            if dir2 == 'dir':
                pprint(files1)
            else:
              #checks if file already exists
                result = client.check('/' + dir + '/' + dir2)
                if result == 'True':
                    print('Error could not make file, it may already exist')
                else:
                    #uploads file
                    client.upload_sync(remote_path='/' + dir + '/' + dir2, local_path="./" + dir2)

    if action == '2':
        print('metadata info -----------------------------------------------------  Remember, "dir" in all inputs to see all home directories')
        run = True
        if run == True:
            client = Client(options)
            client.verify = True
            files1 = client.list()
            pprint(files1)
            print('-----------------------------------------------------------------------------------------------------------------------------------')
        client = Client(options)
        client.verify = True
        infodir = input('file directory (example: hello/dog.gif): ')
        if infodir == "dir":
            files1 = client.list()
            pprint(files1)
        else:
            info = client.info(infodir)
            print(info)


    if action == '6':
        print('List Directories ------------------------------------- Remember, "dir" in all inputs to see most home directories')
        client = Client(options)
        client.verify = True
        files1 = client.list()
        pprint(files1)
        while 1:
            os.system("python main.py")
            print("Restarting...")
            time.sleep(0.2)
        print('--------------------------------------------------------------------------------------------------------------------')
        num = 10
        for x in range(num):
            print('-')
            print('-')
        quit()



#hi lol

    if action == '3':
        print(' make directory ----------------------------------------------------  Remember, "dir" in all inputs to see all home directories')
        run = True
        if run == True:
            client = Client(options)
            client.verify = True
            files1 = client.list()
            pprint(files1)
            print('-----------------------------------------------------------------------------------------------------------------------------------')
        dirname = input('Directory name: ')
        dirpath = input('Directory Path: ')
        if dirname == "dir":
            files1 = client.list()
            pprint(files1)
        else:
            if downloadahh == 'dir':
                pprint(files1)
            else:
                client = Client(options)
                client.verify = True
                client.execute_request('mkdir', "/" + dirpath + '/' + dirname)

    if action == '4':
        print('Check if file already exists ---------------------------------- Remember, "dir" in all inputs to see all home directories')
        run = True
        if run == True:
            client = Client(options)
            client.verify = True
            files1 = client.list()
            pprint(files1)
            print('-----------------------------------------------------------------------------------------------------------------------------------')
        dircheck = input('What directory would you like to check a file in?: ')
        filecheck = input('What file would you like to check?: ')
        if dircheck == "dir":
            files1 = client.list()
            pprint(files1)
        else:
            if filecheck == 'dir':
                pprint(files1)
            else:
                client = Client(options)
                client.verify = True
                result = client.check('/' + dircheck + '/' + filecheck)
                if result == True:
                    print('File already exists!')
                else:
                    print('File does not exist!')

    if action == '5':
        print('Download files from directories ---------------------------------- Remember, "dir" in all inputs to see all home directories')
        run = True
        if run == True:
            client = Client(options)
            client.verify = True
            files1 = client.list()
            pprint(files1)
            print('-----------------------------------------------------------------------------------------------------------------------------------')
        client = Client(options)
        client.verify = True
        dir = input('file directory (leave empty if in root): ')
        downloadahh = input('What file would you like to download?\nplease remember the .filetype (example: dog.gif): ')
        if dir == "dir":
            files1 = client.list()
            pprint(files1)
        else:
            if downloadahh == 'dir':
                pprint(files1)
            else:
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
                        client.download_sync(remote_path=dir + '/' + downloadahh, local_path='new/d~' + name + '.' + filetype)
                        print('new/d~' + name + '.' + filetype)

                        
                        
#-------------------------------------Made By-------------------------------------
#-------------------------------------Cowski!-------------------------------------
#     Cowski#1234 on discord!
