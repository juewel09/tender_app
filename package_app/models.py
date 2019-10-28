from django.db import models
from django.urls import reverse
# Create your models here.
class PE (models.Model):
    pe_name = models.CharField(max_length=100, unique=True, help_text='Enter PE Name')

    def __str__(self):
        return self.pe_name

class Subproject (models.Model):
    subproject_name = models.CharField(max_length=100, unique=True, help_text='Enter Name of the Sub-Project')
    district_name = models.CharField(max_length=100,default='n/a', help_text='Enter Name of the District')
    area = models.IntegerField(default=0, help_text='Enter Area of the Sub-project')

    def __str__(self):
        return self.subproject_name

    def get_absolute_url(self):
        return reverse("package_app:spdetail",kwargs={'pk':self.pk})

class Works (models.Model):
    work_type = models.CharField(max_length=256, unique=True, help_text='Enter Type of the Work')

    def __str__(self):
        return self.work_type

class Contractor (models.Model):
    contractor_name = models.CharField(max_length=100, unique=True, help_text='Enter Name of the Contractor')
    address = models.CharField (max_length= 512, help_text='Enter address of the Contractor')
    email = models.EmailField (unique=True, help_text='Enter e-mail of the Contractor')
    mobile = models.CharField (max_length=50, help_text='Enter mobile number of the Contractor')

    class Meta:
        ordering=['contractor_name']

    def __str__(self):
        return self.contractor_name

class Packages (models.Model):
    package_no = models.CharField(max_length=50, unique=True, help_text='Enter the Package Number')
    package_name = models.CharField (max_length= 1500, help_text='Enter the package name')
    pe = models.ForeignKey(PE, related_name='rnpe', on_delete=models.CASCADE)
    sub_project = models.ForeignKey(Subproject, related_name='rnsubproject',on_delete=models.CASCADE)
    works = models.ForeignKey(Works, related_name='rnworks',on_delete=models.CASCADE)
    contractor_name = models.ForeignKey(Contractor, related_name='rncontractor',on_delete=models.CASCADE)
    estimate_value = models.DecimalField(default=0, max_digits=12, decimal_places=2,help_text='Enter the estimated value')
    contract_value = models.DecimalField(default=0, max_digits=12, decimal_places=2,help_text='Enter the contract prince')
    variation_value = models.DecimalField(default=0, max_digits=12, decimal_places=2,help_text='Enter variation price (if any)of the contract')


    class Meta:
        ordering=['sub_project','works','package_no']

    def get_absolute_url(self):
        return reverse("package_app:packagesdetail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.package_no

    def less_above(self):
        la = ((self.contract_value/self.estimate_value)-1)*100
        if self.contract_value==0:
            result = "The Contract yet not awarded"
        elif la < 0:
            result = str(round(la,2)) + '% Less'
        elif la>0:
            result = str(round(la,2)) + '% Above'
        return result

    def total_cont_value(self):
        value = self.contract_value + self.variation_value
        return value

    def total_expense(self):
        expense_list = Bill.objects.filter(package_no=self)
        total_expense_amount = 0
        for expense in expense_list:
            total_expense_amount+= expense.bill_amount
        return total_expense_amount

class PackageDates (models.Model):
    package_no = models.ForeignKey(Packages, related_name='rnpackages',on_delete=models.CASCADE)
    app_date = models.DateField(null=True, blank=True, help_text='Enter the Anual Procurment Plan approval date')
    ift_date = models.DateField(null=True, blank=True, help_text='Enter the IFT date')
    opening_date = models.DateField(null=True, blank=True, help_text='Enter the tender opening date')
    evaluation_submission_date = models.DateField(null=True, blank=True, help_text='Enter the Evaluation Report submission date')
    evaluation_approval_date = models.DateField(null=True, blank=True, help_text='Enter the Evaluation report approval date')
    adb_concurrence_date = models.DateField(null=True, blank=True, help_text='Enter the ADB concurrence date')
    noa_date = models.DateField(null=True, blank=True, help_text='Enter the Notifcation of Award issuing date')
    contract_sign_date = models.DateField(null=True, blank=True, help_text='Enter the tender submission date')
    start_date = models.DateField(null=True, blank=True, help_text='Enter the Work Starting date as per work order')
    end_date = models.DateField(null=True, blank=True, help_text='Enter the Work Completion date as per work order')
    end_date_extension = models.DateField(null=True, blank=True, help_text='Enter the completion date as per time extension(if any)')
    end_date_actual = models.DateField(null=True, blank=True, help_text='Enter the Actual completion date')

    def __str__(self):
        return str(self.package_no)
    def get_absolute_url(self):
        return reverse("package_app:packagesdetail",kwargs={'pk':self.package_no.pk})


class BillName (models.Model):
    bill_type = models.CharField(max_length=100, unique = True)

    def __str__(self):
        return self.bill_type

class Bill (models.Model):
    package_no = models.ForeignKey(Packages, related_name='rnbill',on_delete=models.CASCADE)
    bill_type = models.ForeignKey(BillName, on_delete=models.CASCADE)
    bill_date = models.DateField(null=True, blank=True, help_text='Enter the Actual Bill payment date')
    bill_amount = models.FloatField(default=0, help_text='Enter the amount of the bill')

    def __str__(self):
        return str(self.package_no)

    def get_absolute_url(self):
        return reverse("package_app:packagesdetail",kwargs={'pk':self.package_no.pk})