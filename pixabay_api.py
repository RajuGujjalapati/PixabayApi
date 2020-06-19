from pixabay import Image, Video
from urllib.request import Request, urlopen
import os
from pathlib import Path
import shutil
import requests as r
API_KEY = os.environ.get('PixabayApiKey')
#IndexError()()()()()()()())())))()()(()()()()()()()()()()
# image operations
image = Image(API_KEY)
# custom image search
q=input("Enter the name as per your requirement:")
ims = image.search(q=str(q),
             lang='en',
             #image_type='photo',
             orientation='horizontal',
             category='butterfly',
             #safesearch='true',
             order='latest',
             page=1,)
             #per_page=3)

print(ims['hits'])
url = [ims['hits'][i]['largeImageURL'] for i in range(3)]#as per the user requirement
print(url)
def total_images(num):
    url = [ims['hits'][i]['largeImageURL'] for i in range(num)]
    return url
user_name = input("Enter Your name :")
    
username=str(user_name)
Path(username).mkdir(parents=True, exist_ok =True)
user_input=input("Enter the folder name what you want to name it:")
with open ('data.txt', 'a') as f:
    f.write(user_input)
    f.write('\n')
    if user_input in 'data.txt':
        pass
    else:
        filename = str(user_input)
        Path(username+'/'+filename).mkdir(parents=True, exist_ok =True)
    
for i in range(len(url)):
    #open the destination file in wb mode.
    x=f"(os.getcwd()+'/{username}'+'/'+filename+'/{i}_{q}.jpg')"
    save_img=open(x,'wb')
    print("save_img",save_img)
    req = r.get(url[i],stream = True)
    print((req.raw))
    #save this raw file into destination.
    shutil.copyfileobj(req.raw,save_img)

