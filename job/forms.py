from django import forms

from job.models import Job


class AddJobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ['job_name', 'job_manager', 'job_start_date',
                  'job_end_date', 'get_in_time']
