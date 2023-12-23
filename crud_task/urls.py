from django.urls import path
from . import views  
from .views import *
urlpatterns=[
    # path('',views.homepage,name="homepage"),
    path('',createtask.as_view(),name='createtask'),
    # path('createtask/',views.createtask,name='createtask'),
    # path('createtask/<int:pk>/',views.update_task,name='updatetask'),
    path('<int:pk>/',views.update_task.as_view(),name='updatetask'),
    
 
]
