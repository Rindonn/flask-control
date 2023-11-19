'''
Author: Rindon
Date: 2023-11-19 13:22:10
LastEditors: Rindon
LastEditTime: 2023-11-19 13:39:44
Description: file check function for server using
FilePath: \flask-control\file_check.py
'''
import os
import time
#检查本地文件夹里是否有文件，在这里可以用永真来检测，检测不到就continue，检测到就送进模型预测
def check_files_in_folder(folder_path):
    #这里的files是个list对象
    files = os.listdir(folder_path)
    
    if not files:
        print("Folder is empty!!")
    elif len(files) > 1:
        print("The number of files is ERROR!\n" + str(len(files)) + " FILES ARE HERE!")
    else:
        #print(files)
        return files

folder_path = "C:\\Users\\rinnd\\Documents\\pi\\pi-photo\\test_folder\\"

file_Name = check_files_in_folder(folder_path)
#在这里可以拼出来完整的本地文件路径
if file_Name:
    file_Path = folder_path + str(file_Name[0])
    print(file_Path)
#目前进展：判断文件夹下是否有文件，有的话判断数量是否为1，为1时返回文件名，拼出完整路径

print("操作中!")
time.sleep(1)
os.remove(file_Path)
print(file_Name[0] + " is deleted!")
#delete over