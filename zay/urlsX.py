from django.urls import path
from . import views


urlpatterns = [
    path('', views.acceuil, name='acceuil'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('contact/', views.contact, name='contact'),

    # path('add/', views.add, name='add'),
    # path('add/addrecord/', views.addrecord, name='addrecord'),
    # path('delete/<int:id>', views.delete, name='delete'),
    # path('update/<int:id>', views.update, name='update'),
    # path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]