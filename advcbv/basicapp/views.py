from django.shortcuts import render
from basicapp.models import school, student
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
# from django.http import HttpResponse

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.school
    template_name = 'basicapp/schoollist.html'
    # return a list as 'school_list'

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.school
    template_name = 'basicapp/schooldetail.html'

class IndexView(TemplateView):
    template_name = 'basicapp/index.html'

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.school
    template_name = 'basicapp/school_form.html'

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.school
    template_name = 'basicapp/school_form.html'

class SchoolDeleteView(DeleteView):
    # fields = ('name', 'principal')
    model = models.school
    # template_name = 'basicapp/schoollist.html'
    success_url = reverse_lazy('basicapp:list')




#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['injectme'] = 'Manish Bainsla'
#         return context

# class CBView(View):
#     def get(self, request):
#         return HttpResponse('CLASS BASED VIEWS ARE COOL..')

# # Create your views here.
# def index(request):
#     return render(request, 'basicapp/index.html', context=None)
