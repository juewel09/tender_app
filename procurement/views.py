import json
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.db.models import Sum, Avg,Count
from package_app.models import Packages, PE, Subproject, Bill
from django.contrib.auth.mixins import LoginRequiredMixin

class TestPage(LoginRequiredMixin,TemplateView):
    template_name = 'test.html'

    def get_context_data(self,**kwargs):
        pe_summary = Packages.objects.values('pe__pe_name').annotate(pe_estimate=(Sum('estimate_value'))/100000 \
                ,pe_contract=(Sum('contract_value')+Sum('variation_value'))/100000,quantity=Count('package_no')) \
                .order_by('pe__pe_name')
        categories = list()
        estimate_series_data = list()
        contract_series_data = list()
        for entry in pe_summary:
            categories.append(entry['pe__pe_name'])
            estimate_series_data.append(int(entry['pe_estimate']))
            contract_series_data.append(int(entry['pe_contract']))
        estimate_series = {
            'name': 'Estimated Cost',
            'data': estimate_series_data,
        }
        contract_series = {
            'name': 'Contract Value',
            'data': contract_series_data,
        }
        chart = {
            'chart': {'type': 'column'},
            'title': {'text': 'PE wise Estimated Cost & Contract Value'},
            'xAxis': {'categories': categories},
            'yAxis': {'title': {'text': 'Cost in Lakh Tk'}},
            'series': [estimate_series, contract_series]
        }
        dump = json.dumps(chart)

        pe_summary1 = Packages.objects.values('pe__pe_name').filter(contract_value__gt=0) \
                .annotate(pe_estimate=(Sum('estimate_value'))/100000,pe_contract=(Sum('contract_value')+Sum('variation_value'))/100000, \
                quantity=Count('package_no')).order_by('-pe_estimate')
        categories1 = list()
        contract1_series_data = list()
        for entry in pe_summary1:
            categories1.append(entry['pe__pe_name'])
            contract1_series_data.append(int(entry['pe_contract']))
        chart1 = {
            'chart': {'type': 'pie'},
            'title': {'text': 'PE wise Contract Value (In Lakh Taka)'},
            'tooltip': {'pointFormat': '{series.name}: <b>{point.percentage:.1f}%</b>'},
            'plotOptions': {'pie': {'allowPointSelect': 'true',
                                    'cursor': 'pointer',
                                    'dataLabels': {'enabled': 'true',
                                    'format': '<b>{point.name}</b>: {point.percentage:.1f} %'}}},
            'series': [{ 'name': 'contract value,',
                        'colorByPoint': 'true',
                        'data': list(map(lambda row: {'name': row['pe__pe_name'], 'y': int(row['pe_contract'])}, pe_summary1))
                        }]
        }
        dump1 = json.dumps(chart1)


        peq = Packages.objects.all().aggregate(etotal=Sum('estimate_value')/100000,ctotal=Sum('contract_value')/100000,quantity=Count('package_no'))

        peq1 = Packages.objects.filter(contract_value__gt=0).aggregate(etotal=Sum('estimate_value')/100000,ctotal=Sum('contract_value')/100000,quantity=Count('package_no'))

        sp_summary = Packages.objects.values('sub_project__subproject_name').annotate(sp_estimate=(Sum('estimate_value'))/100000 \
                ,sp_contract=(Sum('contract_value')+Sum('variation_value'))/100000,quantity=Count('package_no')) \
                .order_by('-sp_estimate')
        sp_summary1 = Packages.objects.values('sub_project__subproject_name').filter(contract_value__gt=0) \
                    .annotate(sp_estimate=(Sum('estimate_value'))/100000 \
                ,sp_contract=(Sum('contract_value')+Sum('variation_value'))/100000,quantity=Count('package_no')) \
                .order_by('-sp_estimate')
        expense = Bill.objects.values('package_no__works__work_type','FY').annotate(total=Sum('bill_amount')).order_by('package_no__works__work_type','FY')




        context  = super().get_context_data(**kwargs)
        context['pe_summary'] = pe_summary
        context['pe_summary1'] = pe_summary1
        context['peq'] = peq
        context['peq1'] = peq1
        context['sp_summary'] = sp_summary
        context['sp_summary1'] = sp_summary1
        context['expense'] = expense
        context['chart'] = dump
        context['chart1'] = dump1
        return context


class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = 'index.html'


    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("test"))
        return super().get(request, *args, **kwargs)
