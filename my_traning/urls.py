from django.urls import path
from . import views

urlpatterns = [
    # path("iii",views.test, name="test"),
    path("about",views.about, name="about"),
    path("",views.index, name="index"),
    #  path("price",views.price, name="price"),
    # path("service",views.service, name="service"),
    path("speed",views.speed, name="speed"),
    path("radio",views.radio, name="radio"),
    path("radio b",views.radiob, name="radio b"),
     path("speed b",views.speedb, name="speed b"),
     path("cloud b",views.cloudb, name="cloud b"), 
    path("data b",views.datab, name="data b"),
     path("voip b",views.voipb, name="voip b"),
    path("coverage",views.coverage, name="coverage"),
    path("contact",views.contact, name="contact"),
     path('email_sender/',views.email_sender,name='email_sender')
    
]
