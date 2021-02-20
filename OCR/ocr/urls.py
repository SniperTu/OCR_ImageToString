from django.urls import path
from app.views import home
from app.views import read_css, read_js, read_img
from app.views import ocrDetect

urlpatterns = [
    path('', home, name='home'),
    path('css/<str:filename>', read_css, name='read_css'),
    path('img/<str:filename>', read_img, name='read_img'),
    path('js/<str:filename>', read_js, name='read_js'),
    path('ocr/', ocrDetect, name='ocrDetect'),      # 在线中文字符识别API
]
