from django.contrib import admin
from package_app.models import Bill, BillName, Contractor, PE, Packages, PackageDates, Subproject, Works,FileCategory,FileUp

admin.site.register(PE)
admin.site.register(Subproject)
admin.site.register(Works)
admin.site.register(Contractor)
admin.site.register(Packages)
admin.site.register(PackageDates)
admin.site.register(BillName)
admin.site.register(FileUp)
admin.site.register(FileCategory)

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('package_no', 'bill_type', 'bill_amount','bill_date')
