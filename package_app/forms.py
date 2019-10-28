# from .widgets import BootstrapDateTimePickerInput
from django import forms
from .models import PackageDates, Bill

class PackageDatesCreateForm(forms.ModelForm):
    class Meta:
        model = PackageDates
        fields = '__all__'

        widgets = {
            'app_date': forms.DateInput(format=('%m/%d/%Y'),
            attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'ift_date': forms.DateInput(format=('%m/%d/%Y'),
            attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'opening_date': forms.DateInput(format=('%m/%d/%Y'),
            attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'evaluation_submission_date': forms.DateInput(format=('%m/%d/%Y'),
            attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'evaluation_approval_date': forms.DateInput(format=('%m/%d/%Y'),
            attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'adb_concurrence_date': forms.DateInput(format=('%m/%d/%Y'),
            attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'noa_date': forms.DateInput(format=('%m/%d/%Y'),
            attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'contract_sign_date': forms.DateInput(format=('%m/%d/%Y'),
            attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'start_date': forms.DateInput(format=('%m/%d/%Y'),
            attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'end_date': forms.DateInput(format=('%m/%d/%Y'),
            attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'end_date_extension': forms.DateInput(format=('%m/%d/%Y'),
            attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'end_date_actual': forms.DateInput(format=('%m/%d/%Y'),
            attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    }

class BillCreateForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = '__all__'

        widgets = {
            'bill_date': forms.DateInput(format=('%m/%d/%Y'),
            attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
