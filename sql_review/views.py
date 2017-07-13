# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import MySQLdb
from MySQLdb.constants.CLIENT import MULTI_STATEMENTS, MULTI_RESULTS
from django.http.response import HttpResponse

from django.shortcuts import render
from django.views import View

# Create your views here.


def review(request):
    file_object = open('public/sql_review.txt')
    try:
        all_the_text = file_object.read()
    finally:
        file_object.close()
    try:
        conn = MySQLdb.connect(host='172.16.169.131', user='', passwd='', db='', port=6666,
                               client_flag=MULTI_STATEMENTS | MULTI_RESULTS)
        cur = conn.cursor()
        ret = cur.execute(all_the_text)
        num_fields = len(cur.description)
        field_names = [i[0] for i in cur.description]
        result = cur.fetchall()
        cur.close()
        conn.close()
        data = {
            'field_names': field_names,
            'result': result
        }
        return render(request, 'sql_review/result.html', data)
    except MySQLdb.Error as e:
        return HttpResponse('Mysql Error {}: {}'.format(e.args[0], e.args[1]), status=500)


class StepView(View):
    def get(self, request):
        data = {
            'sub_module': '2_1'
        }
        return render(request, 'sql_review/step.html', data)
