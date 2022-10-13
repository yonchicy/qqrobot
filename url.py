
from audioop import reverse
from operator import imod
from xml.etree.ElementTree import tostring
import requests
import json
import os
random_url = "https://iw233.cn/api.php?sort=random&type=json"

photo_dir = "./asserts/"
def get_pic_url_list_from_api(url):
    req = requests.get(url,timeout = 3000)
    req_json = req.json()
    return req_json['pic']

def download_pic_from_url_list(pic_url_list):
    pic_num = 0
    for pic_url in pic_url_list:
        # print("pic url is "+pic_url)
        photo_surfix = "" 
        for i in range(0,len(pic_url)):
            if pic_url[-i-1] == '.':
                photo_surfix = pic_url[-i-1:]
                break
        # print("surfix is " + photo_surfix)
        r = requests.get(pic_url,timeout=5000)
        photo_name = photo_dir+"img"+str(pic_num)+photo_surfix
        # print("name is " +photo_name)
        with open(photo_name,'wb') as f:
            f.write(r.content)


def get_pictures():
    pic_url_list = get_pic_url_list_from_api(random_url)
    download_pic_from_url_list(pic_url_list)
def delete_pictures():
    for root,dirs ,files in os.walk(photo_dir):
        for file in files:
            os.remove(os.path.join(root,file))
    
def test():
    a = "abcdefg"
    for i in range(0,len(a)):
        # print(i,a[-i-1])
        if a[-i-1] == 'd':
            # print(a[-i-1:])
            break
    
if __name__== "__main__":
    # pic_url_list = get_pic_url_list_from_api(random_url)
    # download_pic_from_url_list(pic_url_list)
    delete_pictures()

