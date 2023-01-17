from django.urls import path

from user import views

urlpatterns = [
    path('', views.index,name='index'),
    path('details/<int:id>',views.productDetails,name='details'),
    path('reviewprocess/<int:proid>',views.reviewProcess,name='reviewprocess'),
    path('checkout/<int:proid>',views.checkout,name='checkout'),
    path('checkoutprocess/<int:proid>',views.checkoutProcess,name='checkoutprocess'),
]