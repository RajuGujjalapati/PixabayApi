from pixabay import Image, Video
from urllib.request import Request, urlopen
import os
from pathlib import Path
import shutil
import requests as r
from datetime import datetime
# API_KEY = os.environ.get('PixabayApiKey')
# IndexError()()()()()()()())())))()()(()()()()()()()()()()
# image operations
image = Image('20345525-9afec8866713c7dd8d4dd5aee')
# custom image search
q = input("Enter the name of the image you want:")

for i in range(1,10):
    page_no = i
    ims = image.search(q=str(q),
                       lang='en',
                       # image_type='photo',
                       orientation='horizontal',
                       category='dog',
                       # safesearch='true',
                       order='latest',
                       page=int(i), )
    # per_page=3)
    try:
        print(ims['hits'])
        url = [ims['hits'][i]['largeImageURL'] for i in range(5)]  # as per the user requirement
        print(url)
    except IndexError:
        continue


    def total_images(num):
        url = [ims['hits'][i]['largeImageURL'] for i in range(num)]
        return url


    filename = "ImagePixabay"
    Path(filename).mkdir(parents=True, exist_ok=True)
    # a = input("Enter the user name:")

    # data.txt is to append the filenames
    with open('data.txt', 'a') as f:
        f.write(str(f'{q}_{page_no}'))
        f.write('\n')
        if str(f'{q}_{page_no}') in 'data.txt':
            pass
        else:
            filename = str(f'{q}_{page_no}')
            Path(filename).mkdir(parents=True, exist_ok=True)

    for i in range(len(url)):
        # open the destination file in wb mode.
        save_img = open(os.getcwd() + '/' + filename + '/{}_{}_{}.jpg'.format(i, q, datetime.now()), 'wb')
        print("save_img", save_img)
        req = r.get(url[i], stream=True)
        print((req.raw))
        # save this raw file into destination.
        shutil.copyfileobj(req.raw, save_img)