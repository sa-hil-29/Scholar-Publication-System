from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.home, name='home'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('faculty_papers_view',views.faculty_papers_view,name='faculty_papers_view'),
    # path('activate/<uidb64>/<token>',views.activate,name='activate'),
]