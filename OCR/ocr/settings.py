import os
# 设置项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 加密签名
SECRET_KEY = 'b!iohd&_vv@gmva5b6gq@k9t01_k^52uludvw8@h0)1fnez^8l'
DEBUG = True                # 设置当前为调试模式
INSTALLED_APPS = ['app']    # 添加应用
ROOT_URLCONF = 'ocr.urls'   # 设置项目路由文件urls
