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
    
filename="ImagePixabay"
Path(filename).mkdir(parents=True, exist_ok =True)
a=input("Enter the user name:")
with open ('data.txt', 'a') as f:
    f.write(a)
    f.write('\n')
    if a in 'data.txt':
        pass
    else:
        filename = str(a)
        Path(filename).mkdir(parents=True, exist_ok =True)
    
for i in range(len(url)):
    #open the destination file in wb mode.
    save_img=open(os.getcwd()+'/'+filename+'/{}_{}.jpg'.format(i,q),'wb')
    print("save_img",save_img)
    req = r.get(url[i],stream = True)
    print((req.raw))
    #save this raw file into destination.
    shutil.copyfileobj(req.raw,save_img)

