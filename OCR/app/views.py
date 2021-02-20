from django.http import HttpResponse
import numpy as np
import urllib
import json
import cv2
import pytesseract
from PIL import Image
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def read_css(request, filename):
    with open('frontend/css/{}'.format(filename), 'rb') as f:
        css_content = f.read()
        print('css文件')
        return HttpResponse(content=css_content, content_type='text/css')


def read_js(request, filename):
    with open('frontend/js/{}'.format(filename), 'rb') as f:
        js_content = f.read()
    print('js文件')
    return HttpResponse(content=js_content, content_type='application/JavaScript')


def read_img(request, filename):
    with open('frontend/img/{}'.format(filename), 'rb') as f:
        img_content = f.read()
    print('img文件')
    return HttpResponse(content=img_content, content_type='image/jpeg')


def home(request):
    with open('frontend/index.html', 'rb') as f:
        html = f.read()
    return HttpResponse(html)


def read_image(stream=None):
    data_temp = stream.read()
    image = np.asarray(bytearray(data_temp), dtype='uint8')
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image


@csrf_exempt        # 用于规避站点请求攻击
def ocrDetect(request):
    result = {'code': None}
    if request.method == "POST":
        if request.FILES.get("image", None) is not None:
            img = read_image(stream=request.FILES["image"])
        # OpenCV转PIL
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        # 执行识别
        code = pytesseract.image_to_string(img, lang='chi_sim')
        result.update({"output": code})
    return JsonResponse(result)
