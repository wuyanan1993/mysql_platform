# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
import MySQLdb
from MySQLdb.constants.CLIENT import MULTI_STATEMENTS, MULTI_RESULTS
from django.http.response import HttpResponse

from django.shortcuts import render
from django.views import View
from django.core import serializers

from statistics.models import MysqlInstance, MysqlInstanceGroup
from sql_review.models import SqlReviewRecord
from sql_review.forms import SqlReviewRecordForm

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
        instance_groups = MysqlInstanceGroup.objects.all()
        data = {
            'sub_module': '2_1',
            'instance_groups': instance_groups,
            'start_time': datetime.now().strftime('%Y-%m-%d %H:%M')
        }
        return render(request, 'sql_review/step.html', data)

    def post(self, request):
        print(request.POST)
        sql_review_form = SqlReviewRecordForm(request.POST)
        if sql_review_form.is_valid():
            print('success')
        else:
            # print(sql_review_form)
            pass
        return HttpResponse('ok', status=200)


def instance_by_ajax_and_id(request):
    group_id = request.POST.get('group_id', '1')
    instance = MysqlInstance.objects.filter(group=group_id)
    return HttpResponse(serializers.serialize("json", instance), content_type='application/json')
