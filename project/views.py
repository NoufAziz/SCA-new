from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views import generic
from project.models import Subject, Cource, Lecture, Comment_l, Comment_c
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from .forms import Userform
from django.http import HttpResponseRedirect

class UserFormView(View):
    form_class = Userform
    template_name= 'project/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user= form.save(commit=False)

            username = form.clean_data['username']
            password = form.clean_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('project:index')
        return render(request, self.template_name, {'form':form})

class IndexView(generic.ListView):
    template_name = 'project/index.html'
    context_object_name = 'all_subjects'
    def get_queryset(self):
        return Subject.objects.all()

class SubjectView(generic.ListView):
    template_name = 'project/subject.html'
    context_object_name = "Subject"
    def get_queryset(self):
        return Cource.objects.all()

class ShowSubjectView(generic.DetailView):
    model = Subject
    template_name = 'project/subject.html'
    context_object_name = "Subject"
    pk_url_kwarg = "subject_id"
    query_pk_and_slug = True

class CourceView(generic.ListView):
    template_name = 'project/cource.html'
    context_object_name = "Cource"
    def get_queryset(self):
        return Lecture.objects.all()

class ShowCourceView(generic.DetailView):
    model = Cource
    template_name = 'project/cource.html'
    context_object_name = "Cource"
    pk_url_kwarg = "cource_id"
    query_pk_and_slug = True

class ShowLectureView(generic.DetailView):
    model = Lecture
    template_name = 'project/show_lecture.html'
    context_object_name = "Lecture"
    pk_url_kwarg = "lecture_id"
    query_pk_and_slug = True



class CourceCreate(CreateView):
    model = Cource
    fields = ['subject','title', 'description', 'location' ]
    success_url = reverse_lazy('project:index')
    pk_url_kwarg = "cource_id"
    query_pk_and_slug = True
class CourceUpdate(UpdateView):
    model = Cource
    fields = ['subject','title', 'description', 'location' ]
    success_url = reverse_lazy('project:index')
    pk_url_kwarg = "cource_id"
    query_pk_and_slug = True
class CourceDelete(DeleteView):
    model = Cource
    success_url = reverse_lazy('project:index')
    pk_url_kwarg = "cource_id"
    query_pk_and_slug = True

class LectureCreate(CreateView):
    model = Lecture
    fields = ['cource','title', 'sources','objectives', 'link' ]
    success_url = reverse_lazy('project:index')
    pk_url_kwarg = "lecture_id"
    query_pk_and_slug = True
class LectureUpdate(UpdateView):
    model = Lecture
    fields = ['cource','title', 'sources','objectives', 'link' ]
    success_url = reverse_lazy('project:index')
    pk_url_kwarg = "lecture_id"
    query_pk_and_slug = True
class LectureDelete(DeleteView):
    model = Lecture
    success_url = reverse_lazy('project:index')
    pk_url_kwarg = "lecture_id"
    query_pk_and_slug = True


class CourceComment(CreateView):
    model = Comment_c
    fields = ['cource','author', 'body' ]
    success_url = reverse_lazy('project:index')
    pk_url_kwarg = "cource_id"
    context_object_name = "Cource"
    query_pk_and_slug = True

def comment_c(request, cource_id):
    cource= get_object_or_404(Cource, id=cource_id)
    cource.comment_l_set.all()
    user_comment=request.POST['comment']
    author = request.POST['author']
    comment_c.objects.create(
        cource=cource,
        author=author,
        body=user_comment,
    )
    return HttpResponseRedirect(reverse('show_cource', args=(cource_id)))


class LectureComment(CreateView):
    model = Comment_l
    fields = ['lecture','author', 'body' ]
    success_url = reverse_lazy('project:index')
    pk_url_kwarg = "lecture_id"
    context_object_name = "Lecture"
    query_pk_and_slug = True


def comment_l(request, lecture_id):
    lecture= get_object_or_404(Lecture, id=lecture_id)
    lecture.comment_l_set.all()
    user_comment=request.POST['comment']
    author = request.POST['author']
    comment_l.objects.create(
        lecture=lecture,
        author=author,
        body=user_comment,
    )
    return HttpResponseRedirect(reverse('show_lecture', args=(lecture_id)))
