from django.urls import path

from super import views

urlpatterns = [
    path('addproduct', views.addproduct,name='addproduct'),
    path('addproductprocess', views.addproductProcess,name='addproductprocess'),
    path('',views.loginPage,name='login'),
    path('loginprocess',views.loginProcess,name='loginprocess'),
    path('products',views.products,name='products'),
    path('editproduct/<int:id>',views.editProduct,name='editproduct'),
    path('deleteproduct/<int:id>',views.deleteProduct,name='deleteproduct'),
    path('updateproduct/<int:id>',views.updateProduct,name='updateproduct'),
    path('orders',views.viewOrders,name='orders'),
    path('findproduct/<int:proid>',views.findProduct,name='findproduct'),
    path('approve/<int:id>/<int:proid>',views.approve,name='approve'),
    path('dontapprove/<int:id>/<int:proid>',views.dontapprove,name='dontapprove'),
    path('reviews',views.reviews,name='reviews'),
    path('logout',views.logout1,name='logout')
]