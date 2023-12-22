from django.urls import path
from . import views
urlpatterns=[
    path('',views.homepage,name="homepage"),
    path('createtask/',views.createtask,name='createtask'),
    path('updatetask/<int:pk>/',views.update_task,name='updatetask'),
    
 
]
