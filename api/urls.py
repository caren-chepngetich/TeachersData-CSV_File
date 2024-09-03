
from django.urls import path
from .views import TeacherListView
from .views import TrainerListView
from .views import KicdofficialListView


urlpatterns =[
    path("trainer/",TrainerListView.as_view(),name="trainer_list_view"),
    path("teacher/",TeacherListView.as_view(),name="teacher_list_view"),
    path("course/",KicdofficialListView.as_view(),name="kicdofficial_list_view"),
]