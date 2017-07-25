# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
import MySQLdb
import json
from MySQLdb.constants.CLIENT import MULTI_STATEMENTS, MULTI_RESULTS
from django.http.response import HttpResponse, HttpResponseRedirect

from django.shortcuts import render
from django.views import View
from django.core import serializers

from mysql_platform.settings import INCEPTION_IP, INCEPTION_PORT
from statistics.models import MysqlInstance, MysqlInstanceGroup
from sql_review.models import SqlReviewRecord
from sql_review.forms import SqlReviewRecordForm

# Create your views here.


def review(request, record_id):
    record = SqlReviewRecord.objects.get(id=record_id)
    sql = record.sql
    instance = record.instance
    instance_ip = instance.ip
    instance_port = instance.port
    all_the_text = message_to_review_sql(host=instance_ip, port=instance_port, sql=sql)
    try:
        conn = MySQLdb.connect(host=INCEPTION_IP, user='', passwd='', db='', port=INCEPTION_PORT,
                               client_flag=MULTI_STATEMENTS | MULTI_RESULTS)
        cur = conn.cursor()
        ret = cur.execute(all_the_text)
        num_fields = len(cur.description)
        field_names = [i[0] for i in cur.description]
        result = cur.fetchall()
        # 判断结果中是否有error level 为 2 的，如果有，则不做操作，如果没有则将sql_review_record 记录的 is_checked 设为1
        flag = 'success'
        for res in result:
            if res[2] == 2:
                flag = 'failed'
        if flag == 'success':
            record.is_checked = 1
            record.save()
        cur.close()
        conn.close()
        data = {
            'field_names': field_names,
            'result': result,
            'sub_module': '2_1',
            'flag': flag,
            'record_id': record.id
        }
        return render(request, 'sql_review/result.html', data)
    except MySQLdb.Error as e:
        return HttpResponse('Mysql Error {}: {}'.format(e.args[0], e.args[1]), status=500)


def message_to_review_sql(host, port, sql):
    review_sql = """
    /*--user=inception;--password=inception;--host=""" + host + """;--enable-check;--port=""" + str(port) + """;--disable-remote-backup;*/
inception_magic_start;
""" + sql + """
inception_magic_commit;    
    """
    return review_sql


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
        sql_review_form = SqlReviewRecordForm(request.POST)
        if sql_review_form.is_valid():
            result = SqlReviewRecord()
            # result.save()
            result.sql = sql_review_form.cleaned_data.get('sql')
            result.for_what = sql_review_form.cleaned_data.get('for_what')
            result.instance = sql_review_form.cleaned_data.get('instance')
            result.instance_group = sql_review_form.cleaned_data.get('instance_group')
            result.execute_time = sql_review_form.cleaned_data.get('execute_time')
            result.save()
            data = {
                'result': 'success',
                'result_id': result.id
            }
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            data = {
                'result': 'error'
            }
            return HttpResponse(json.dumps(data), content_type='application/json')


def instance_by_ajax_and_id(request):
    group_id = request.POST.get('group_id', '1')
    instance = MysqlInstance.objects.filter(group=group_id)
    return HttpResponse(serializers.serialize("json", instance), content_type='application/json')


def submitted_list(request):
    # 取出账号权限下所有的审核请求
    record_list = SqlReviewRecord.objects.filter(is_checked=1).order_by('-id')
    data = {
        'record_list': record_list,
        'sub_module': '2_2'
    }
    return render(request, 'sql_review/record_list.html', data)
