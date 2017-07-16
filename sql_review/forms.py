from django import forms

from sql_review.models import SqlReviewRecord


class SqlReviewRecordForm(forms.ModelForm):
    class Meta:
        model = SqlReviewRecord
        fields = ['for_what', 'instance_group', 'instance', 'execute_time', 'sql']
