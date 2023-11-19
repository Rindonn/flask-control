#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@ Author: Rindon
@ Date: 2023-11-10 16:26:16
LastEditors: Rindon
LastEditTime: 2023-11-18 13:23:07
@ Description: FTP module for piTank
'''
from ftplib import FTP
import os 
import time
from picamera import PiCamera

class pi_Photo():
    '''
        description:'Class for pi connect to ftp server and take photos.',
    '''
    def __init__(self):
        '''
            description:'Config for ftp',
            param:' address : server IP address,
                    port : server ftp port number,
                    username : ftp username,
                    password : ftp password,
                    remote_Path : where you want to upload in ftp server,
                    local_Path : where you want to save photos in pi,
                    bufsize : set bufsize when upload to ftp server,
                    ftp : a object of FTP class for saving login attribute',
            return:'None'
        '''
        self.address = "192.168.137.1"
        self.port = int(21)
        self.username = "ftpuser"
        self.password = "ftpuser"
        self.remote_Path = "/pi-photo/"
        self.local_Path = "/home/pi/flask-control/photo/"
        self.bufsize = int(1024)
        self.ftp = FTP()

    def ftp_Link(self):
        '''
            description:'connect to ftp server',
            param:'None'
            return:'login success or not'
        '''
        try:
            self.ftp.connect(host = self.address,port = self.port)
            self.ftp.login(self.username,self.password)
            print('Login success!',self.ftp.login(self.username,self.password))
        except:
            print('Login failed!',self.ftp.login(self.username,self.password))

    def ftp_Upload(self,number,control):
        '''
            description:'take photos and upload to ftp server with two steps.',
            param:'number : flag for not rewrite,
                   control : save photos to different folders for training.'
            return:'None'
        '''
        #first step:capture
        camera = PiCamera()
        folder_Path = self.local_Path + control + '/'
        if not os.path.exists(folder_Path):
            os.makedirs(folder_Path)
        file_Name = "%s_image_%s.jpg" % (number,time.time())
        file_Path = folder_Path + file_Name
        #take a photo and save
        camera.capture(file_Path)
        #second step:upload
        file = open(file_Path, 'rb')
        refolder_Path = self.remote_Path + control + '/'
        #print(FTP.dir(self.ftp))
        #print(refolder_Path)
        #print(self.ftp.cwd(refolder_Path))
        try:
            self.ftp.storbinary('STOR ' + refolder_Path + file_Name,file)
        except:
            print("Upload error! Check permission or network!")
        file.close()
        camera.close()

    def ftp_Close(self):
        '''
            description:'disconnect to ftp server',
            param:'None'
            return:'None'
        '''
        self.ftp.quit()

    

if __name__ == "__main__":
    #ftp connect check
    upload = pi_Photo()
    upload.ftp_Link()
    upload.ftp_Close()