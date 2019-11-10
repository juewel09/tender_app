from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from .forms import PackageDatesCreateForm, BillCreateForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from package_app.models import Packages, Subproject
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin

class SubprojectListView(ListView):
    model=models.Subproject

class SubprojectDetailView(DetailView):
    model=models.Subproject
    template_name = 'package_app/subproject_detail.html'

class WorksListView(ListView):
    model=models.Works
class WorksDetailView(DetailView):
    model=models.Works
    template_name = 'package_app/works_detail.html'

class PEListView(ListView):
    model=models.PE
class PEDetailView(DetailView):
    model=models.PE
    template_name = 'package_app/pe_detail.html'

class ContractorListView(ListView):
    model=models.Contractor
class ContractorDetailView(DetailView):
    model=models.Contractor
    template_name = 'package_app/contractor_detail.html'

class PackagesListView(ListView):
    model=models.Packages
    # paginate_by = 25


class PackagesDetailView(DetailView):
    model=models.Packages
    template_name = 'package_app/packages_detail.html'

class PackagesCreateView(LoginRequiredMixin,CreateView):
    login_url = 'accounts:login'
    redirect_field_name = 'package_app/packages_detail.html'
    model = models.Packages
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)
class PackageUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'accounts:login'
    redirect_field_name = 'package_app/packages_detail.html'
    model=models.Packages
    fields = '__all__'



class PackageDatesCreateView(LoginRequiredMixin,CreateView):
    login_url = 'accounts:login'
    form_class = PackageDatesCreateForm
    redirect_field_name = 'package_app/packages_detail.html'
    model = models.PackageDates

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)

class PackageDatesUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'accounts:login'
    redirect_field_name = 'package_app/packages_detail.html'
    fields ='__all__'
    model = models.PackageDates

class BillListView(ListView):
    model=models.Bill

class BillCreateView(LoginRequiredMixin,CreateView):
    login_url = 'accounts:login'
    form_class = BillCreateForm
    redirect_field_name = 'package_app/packages_detail.html'
    model = models.Bill

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)

class BillUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'accounts:login'
    redirect_field_name = 'package_app/packages_detail.html'
    model=models.Bill
    fields = '__all__'


class SubprojectCreateView(CreateView):
    model=models.Subproject
    fields = ('subproject_name', 'district_name','area')

class SubprojectUpdateView(UpdateView):
    model=models.Subproject
    fields = ('subproject_name', 'district_name','area')

class SubprojectDeleteeView(DeleteView):
    model=models.Subproject
    success_url = reverse_lazy("package_app:splist")
