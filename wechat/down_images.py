#!usr/bin/env python
# coding=utf-8
# Created by zhezhiyong@163.com on 2016/10/18.

import json
import os
import urllib

BASE_PATH = os.getcwd()
FILE_NAME = "emoticons.json"


def store(data):
    with open('data.json', 'w') as json_file:
        json_file.write(json.dumps(data))


def load(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
        return data


def down_item(url):
    urllib.urlopen(url, )


def process_item(data):
    dir_path = '%s/images' % (BASE_PATH)  # 存储路径
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    for image_dir in data:
        image_url = image_dir.get('url')
        print image_url
        list_name = image_url.split('/')
        image_name = list_name[list_name.__len__() - 2]
        conn = urllib.urlopen(image_url)  # 下载图片
        image_type = conn.info().getheader('Content-Type')
        suffix = image_type.split('/')[1]
        file_path = '%s/%s.%s' % (dir_path, image_name, suffix)
        print image_name
        if os.path.exists(image_name):
            continue
        with open(file_path, 'wb') as file_writer:
            file_writer.write(conn.read())
        file_writer.close()


if __name__ == "__main__":
    # print load(FILE_NAME)
    process_item(load(FILE_NAME))
