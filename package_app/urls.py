from django.urls import path
from package_app import views
app_name = 'package_app'
urlpatterns = [
    path('subproject/',views.SubprojectListView.as_view(), name='splist'),
    path('subproject/<int:pk>/',views.SubprojectDetailView.as_view(), name='spdetail'),
    path('subproject/create/',views.SubprojectCreateView.as_view(),name='spcreate'),
    path('subproject/update/<int:pk>/',views.SubprojectUpdateView.as_view(), name='spupdate'),
    path('subproject/delete/<int:pk>/',views.SubprojectDeleteeView.as_view(), name='spdelete'),
    path('works/',views.WorksListView.as_view(), name='workslist'),
    path('works/<int:pk>/',views.WorksDetailView.as_view(), name='worksdetail'),
    path('pe/',views.PEListView.as_view(), name='pelist'),
    path('pe/<int:pk>/',views.PEDetailView.as_view(), name='pedetail'),
    path('contractor/',views.ContractorListView.as_view(), name='contractorlist'),
    path('contractor/<int:pk>/',views.ContractorDetailView.as_view(), name='contractordetail'),
    path('packages/',views.PackagesListView.as_view(), name='packageslist'),
    path('packages/<int:pk>/',views.PackagesDetailView.as_view(), name='packagesdetail'),
    path('packages/create/',views.PackagesCreateView.as_view(),name='packcreate'),
    path('package/update/<int:pk>/',views.PackageUpdateView.as_view(), name='packageupdate'),
    path('packagedate/create/',views.PackageDatesCreateView.as_view(),name='packdatecreate'),
    path('packagedate/update/<int:pk>/',views.PackageDatesUpdateView.as_view(), name='packagedateupdate'),
    path('bill/create/',views.BillCreateView.as_view(),name='billcreate'),
    path('bill/update/<int:pk>/',views.BillUpdateView.as_view(), name='billupdate'),
    path('bills/',views.BillListView.as_view(), name='billlist'),
    ]
