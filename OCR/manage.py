if __name__ == '__main__':
    import sys
    import django
    import os
    DJANGO_SETTINGS_MODULE = 'ocr.settings'
    # 设置环境变量
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ocr.settings')
    django.setup()
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
