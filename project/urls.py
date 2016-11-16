from django.conf.urls import url
from project import views

app_name = 'project'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    #/StudentsClubAcademy
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    #/StudentsClubAcademy

    url(r'^subject/$', views.SubjectView.as_view(), name='subject'),
    #/StudentsClubAcademy/Subject/

    url(r'^subject/(?P<subject_id>[0-9]+)/$', views.ShowSubjectView.as_view(), name='show_subject'),
    #/StudentsClubAcademy/Subject/1/


    url(r'^subject/(?P<subject_id>[0-9]+)/cource/$', views.CourceView.as_view(), name='cource'),
    #/StudentsClubAcademy/Subject/1/Cource/

    url(r'^subject/(?P<subject_id>[0-9]+)/cource/(?P<cource_id>[0-9]+)/$', views.ShowCourceView.as_view(), name='show_cource'),
    #/StudentsClubAcademy/Subject/1/Cource/1/

    url(r'^cource/add/$', views.CourceCreate.as_view(), name='add-cource'),
    #/StudentsClubAcademy/Subject/1/Cource/add/
    url(r'^subject/(?P<subject_id>[0-9]+)/cource/(?P<cource_id>[0-9]+)/update/$', views.CourceUpdate.as_view(), name='update-cource'),
    #/StudentsClubAcademy/Subject/1/Cource/2/update/
    url(r'^subject/(?P<subject_id>[0-9]+)/cource/(?P<cource_id>[0-9]+)/delete/$', views.CourceDelete.as_view(), name='delete-cource'),
    #/StudentsClubAcademy/Subject/1/Cource/2/delete


    url(r'^subject/(?P<subject_id>[0-9]+)/cource/(?P<cource_id>[0-9]+)/lecture/(?P<lecture_id>[0-9]+)/$', views.ShowLectureView.as_view(), name='show_lecture'),
    #/StudentsClubAcademy/Subject/1/Cource/2/Lecture/1/

    url(r'^lecture/add/$', views.LectureCreate.as_view(), name='add-lecture'),
    #/StudentsClubAcademy/Subject/1/Cource/2/Lecture/add/
    url(r'^subject/(?P<subject_id>[0-9]+)/cource/(?P<cource_id>[0-9]+)/lecture/(?P<lecture_id>[0-9]+)/update/$', views.LectureUpdate.as_view(), name='update-lecture'),
    #/StudentsClubAcademy/Subject/1/Cource/2/Lecture/2/
    url(r'^subject/(?P<subject_id>[0-9]+)/cource/(?P<cource_id>[0-9]+)/lecture/(?P<lecture_id>[0-9]+)/delete/$', views.LectureDelete.as_view(), name='delete-lecture'),
    #/StudentsClubAcademy/Subject/1/Cource/2/Lecture/2/delete


]