# -*- coding: utf-8 -*-   
       
import os  

def file_name(file_dir):
    file_list = []
    for root, dirs, files in os.walk(file_dir):  
        # print(root) #当前目录路径  
        # print(dirs) #当前路径下所有子目录  
        if len(files) > 0:
            for item in files:
                file_list.append(item) #当前路径下所有非目录子文件 
    return file_list

# 获取当前目录
print(os.path.abspath(os.path.dirname(__file__)))
file_list = file_name(os.path.abspath(os.path.dirname(__file__)) + '/source/_posts')
print(file_list)
print(len(file_list))
