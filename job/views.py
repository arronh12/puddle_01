from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Job,JobItems
from item.models import Items
from job.forms import AddJobForm


class JobHomeView(TemplateView):
    template_name = 'job/job_home.html'

    def get(self, request):
        all_jobs = Job.objects.all()
        context = {
            'all_jobs': all_jobs
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        all_jobs = Job.objects.all()
        context = {
            'all_jobs': all_jobs
        }
        return render(request, self.template_name, context)


class AddJobView(TemplateView):
    template_name = 'job/add_job.html'

    def get(self, request):
        form = AddJobForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AddJobForm(request.POST)
        if form.is_valid():
            form.save()

        return render(request, self.template_name, context={'form': form})


def selected_job(request, choice):
    job = Job.objects.all()
    job = Job.objects.get(pk=choice)
    context = {
        'choice': choice,
        'job': job,
    }
    return render(request, 'job/selected_job.html', context)


def add_to_job(request, jobnum):
    items = Items.objects.all()
    job = Job.objects.all()
    newJob = ''
    itemList = JobItems.objects.filter(job_id=jobnum)

    for list_end in itemList:
        new_job = items.filter(item_name__contains=list_end.item_id.item_name)

    job = Job.objects.get(pk=jobnum)
    context = {
        'jobnum': jobnum,
        'job': job,
        'new_job': new_job
    }
    return render(request, 'job/add_to_job.html', context)
