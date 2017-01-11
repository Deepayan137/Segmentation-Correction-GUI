import requests
import json

from os.path import basename
import base64
from PIL import Image
from io import BytesIO
import cv2
import glob, os
import shutil
def request_info(path):
    session = requests.Session()
    session.trust_env = False
    url = 'http://ocr.iiit.ac.in/beta/service/api/segmentation/get/'

    r = session.get(url)
    # print r.status_code
    json_data = r.json()
    print json_data
    json_data = json_data[0]
    id = json_data['id']

    image = json_data['image']
    image_name = str(image).split('/')[-1]

    response = session.get(image)
    i = Image.open(BytesIO(response.content))
    i.save(path + image_name)
    return id


# request_info()
def post_info(id, image, text_file,path):
    state =0
    api_file = path
    session = requests.Session()
    # session.add_header("Content-type", "application/x-www-form-urlencoded; charset=UTF-8")

    session.trust_env = False

    # with open(image, "rb") as image_file:
    # encoded_image = base64.b64encode(image_file.read())
    url2 = 'http://ocr.iiit.ac.in/beta/service/api/segmentation/save/'
    data = {'image': str(id)}
    files = {'fixed_image': open(image, "rb"), 'fixed_segmentation_plot_file': open(text_file, 'rb')}
    r = session.post(url2, files=files, data=data)
    if r.status_code == 200:
        #shutil.rmtree('/home/deepayan/CVIT_codes/API/')

        test = path+'*'
        r = glob.glob(test)
        for i in r:
            os.remove(i)



        state=1
    elif r.status_code == 400:
        state = 2
    elif r.staus_code == 403:
        state = 3
    return state


