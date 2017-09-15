'''
将文件数据导入到数据库
'''
import os
import time

import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oa.settings")
import django
if django.VERSION > (1, 7): #判断版本
    django.setup()


def main():

    from loaddata.models import WorkTime

    os.environ['TZ'] =  'Asia/Shanghai'
    a = datetime.datetime.now()

    dirName = 'media/';
    fileName = '981.txt';
    f = open(dirName+fileName,encoding='utf-8')
    oa_id = fileName.split('.')[0];
    for line in f:
        line = line.rstrip()
        if WorkTime.objects.filter(oa_id=oa_id).filter(clocktime=line) :
            pass
        elif len(line)>1:
            b = WorkTime()
            b.oa_id = oa_id
            b.clocktime = line
            b.save()
    f.close()
    print("共导入" + len(f) +"行")

if __name__ == '__main__':
    main();
    print("Done");

