from django.urls import path, include

from department.views import  slug_view, index_department

urlpatterns = [
    path('department/', include([
        path('<int:id>/', index_department),
        path('<slug:slug>/', slug_view),
    ]))


    #path('department/<slug:slug>/', slug_view),
    #path('department/<id>/', index),


]
