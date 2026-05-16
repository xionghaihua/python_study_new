#通过open
import os

with open('mv.csv',mode="r",encoding="utf-8") as file_object:
    for line in file_object:
        user_id,username,url = line.strip().split(',')
        print(username,url)
 