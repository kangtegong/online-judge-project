import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "uosoj.settings")
import django
django.setup()
from dash.models import Notice
from homework.models import Course
import requests
from xml.etree import ElementTree as ET


def note_get():
    URL = 'http://wise.uos.ac.kr/uosdoc/api.ApiApiMainBd.oapi'

    params = {
        'apiKey' : '201908573UUA27738'	
    }

    response = requests.get(URL, params=params)
    source = response.text
    root = ET.fromstring(source)
    calendar = root.findall('boardList/list')

    # 공지사항 

    for listelem in calendar:
        t = listelem.find('title').text
        nd = listelem.find('notice_dt').text
        ct = listelem.find('content').text
        
        Notice(
            title=t,
            date=nd,
            body=ct,
            by_whom=True
        ).save()
    
    # 학사달력 

    root = ET.fromstring(source)
    lists = root.findall('schList/list')

    for listelem in lists:
        content = listelem.find('content').text
        sch_date = listelem.find('sch_date').text
        year = listelem.find('year').text
        month = listelem.find('month').text

        Notice(
            title=content,
            date=month,
            by_whom=True
        ).save()

    # value 값만 넘기기
    return Notice

def course_get():

    # class list api receive

    URL = 'http://wise.uos.ac.kr/uosdoc/api.ApiUcrMjTimeInq.oapi'

    params = {
        'apiKey' : '201908573UUA27738',
        'year' : '2019',
        'term' : 'A20',
        'deptDiv' : '210', 
        'dept' : 'A200110111',
        'subDept' : 'A200200120',
    }

    response = requests.get(URL, params=params)
    source = response.text

    root = ET.fromstring(source)
    lists = root.findall('.//list')
 
    for listelem in lists:
        sn = listelem.find('subject_nm').text
        cn = listelem.find('class_nm').text
        pn = listelem.find('prof_nm').text
        subn = listelem.find('subject_no').text
        cd = listelem.find('class_div').text
        sy = listelem.find('shyr').text

        Course(
            subject_no=subn, 
            class_div=cd, 
            subject_nm=sn, 
            shyr=sy, 
            prof_nm=pn, 
            class_nm=cn
            ).save()


if __name__=='__main__':
    get = note_get()
    c_get = course_get()
    print("class db 반영 완료")
