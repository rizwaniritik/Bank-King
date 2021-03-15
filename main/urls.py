from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
   path("",views.home,name="home"),
   path("/",views.home,name="home"),
   path('Details',views.Details,name="Details"),
    path('RecentTransactions',views.RecentTransactions,name="RecentTransactions"),
     path('AllTransactions/<int:r>',views.AllTransactions,name="AllTransactions"),
     
      path('fifth',views.fifth,name='fifth'),
      path('transfer/<int:customer_id>',views.transfer,name='transfer'),
]
