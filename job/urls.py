from job.views import JobHomeView, AddJobView
from django.urls import path

from . import views

app_name = "job"

urlpatterns = [
    path('all_jobs/', JobHomeView.as_view(), name='Jobs'),
    path('add_job/', AddJobView.as_view(), name='add_job'),
    path('selected_job/<int:choice>', views.selected_job, name='selected_job'),
    path('add_to_job/<int:jobnum>', views.add_to_job, name='add_to_job'),
]
