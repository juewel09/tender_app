from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.db.models import Sum, Avg,Count
from package_app.models import Packages, PE, Subproject
from django.contrib.auth.mixins import LoginRequiredMixin

class TestPage(LoginRequiredMixin,TemplateView):
    template_name = 'test.html'

    def get_context_data(self,**kwargs):
        pe_summary = Packages.objects.values('pe__pe_name').annotate(pe_estimate=(Sum('estimate_value'))/100000 \
                ,pe_contract=(Sum('contract_value')+Sum('variation_value'))/100000,quantity=Count('package_no')) \
                .order_by('-pe_estimate')
        pe_summary1 = Packages.objects.values('pe__pe_name').filter(contract_value__gt=0) \
                .annotate(pe_estimate=(Sum('estimate_value'))/100000,pe_contract=(Sum('contract_value')+Sum('variation_value'))/100000, \
                quantity=Count('package_no')).order_by('-pe_estimate')
        peq = Packages.objects.all().aggregate(etotal=Sum('estimate_value')/100000,ctotal=Sum('contract_value')/100000,quantity=Count('package_no'))

        peq1 = Packages.objects.filter(contract_value__gt=0).aggregate(etotal=Sum('estimate_value')/100000,ctotal=Sum('contract_value')/100000,quantity=Count('package_no'))

        sp_summary = Packages.objects.values('sub_project__subproject_name').annotate(sp_estimate=(Sum('estimate_value'))/100000 \
                ,sp_contract=(Sum('contract_value')+Sum('variation_value'))/100000,quantity=Count('package_no')) \
                .order_by('-sp_estimate')
        sp_summary1 = Packages.objects.values('sub_project__subproject_name').filter(contract_value__gt=0) \
                    .annotate(sp_estimate=(Sum('estimate_value'))/100000 \
                ,sp_contract=(Sum('contract_value')+Sum('variation_value'))/100000,quantity=Count('package_no')) \
                .order_by('-sp_estimate')
        context  = super().get_context_data(**kwargs)
        context['pe_summary'] = pe_summary
        context['pe_summary1'] = pe_summary1
        context['peq'] = peq
        context['peq1'] = peq1
        context['sp_summary'] = sp_summary
        context['sp_summary1'] = sp_summary1
        return context


class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = 'index.html'


    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("test"))
        return super().get(request, *args, **kwargs)
