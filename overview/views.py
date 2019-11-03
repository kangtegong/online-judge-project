from django.shortcuts import render, get_object_or_404, redirect
import requests
from django.views.generic.list import ListView # 데이터 보여주기
from homework.models import Course

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from xml.etree import ElementTree as ET


@login_required(login_url='/')
def getClass(request, subno):
    URL = 'http://wise.uos.ac.kr/uosdoc/api.ApiApiCoursePlanView.oapi'

    params = {
    'apiKey' : '201908573UUA27738',
	'year' : '2019',
	'term' : 'A20',
	'subjectNo' : subno, 
	'classDiv' : '01'
    }

    response = requests.get(URL, params=params)
    source = response.text

    root = ET.fromstring(source)
    lists = root.findall('.//list')

    for listelem in lists:
        sn = listelem.find('subject_nm').text
        cn = listelem.find('subject_no').text
        pn = listelem.find('prof_nm').text
        tel = listelem.find('tel_no').text
        score = listelem.find('score_eval_rate').text
        book = listelem.find('book_nm').text
        desc = listelem.find('lec_goal_descr').text
        goal = listelem.find('curi_edu_goal_nm').text
        week = listelem.find('week').text
        class_cont = listelem.find('class_cont').text
    
        scores = score.split("□")

        '''
        subject_no : 교과번호
        subject_nm : 교과목명
        prof_nm : 담당 교수 성명
        tel_no : 담당교수 연락처 정보
        score_eval_rate : 성적평가
        book_nm : 교재
        lec_goal_descr : 교과목설명
        curi_edu_goal_nm : 수업목표
        week : 주
        class_cont : (주별) 수업내용 정보
        class_meth : (주별) 수업방법 
        '''
    return render(request, 'overview/overview.html', {
        'sn':sn, 
        'cn':cn, 
        'pn':pn, 
        'tel':tel, 
        'scores':scores, 
        'book':book, 
        'desc':desc, 
        'goal':goal, 
        'week':week
        })

class OverviewList(LoginRequiredMixin, ListView):
    login_url = '/'
    redirect_field_name = '/'
    model = Course
    template_name = 'overview/overviewlist.html'