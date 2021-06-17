"""django_forms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path
from . import views 
from .views import building_upload, buildings_details, aberdeen_site, ashton_site, bournemouth_site, bristol_site, bury_site, cardiff_site 
from .views import cheadle_site, coventry_site, dudley_site, edinburgh_site, elstree_site, farnborough_site, glasgow_site
from .views import heronsreach_site, hull_site, hyde_site, leeds_site, liverpool_whiston_site, maidstone_site, newcastle_site
from .views import nottingham_site, portsmouth_site, solihull_site, southleeds_site, stdavids_site, swansea_site
from .views import swindon_site, walsall_site, warrington_site, wirral_site

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('upload-csv/', building_upload, name="building_upload"),
    path('building/', buildings_details, name="building_details" ),
    path('', views.HomeView.as_view()), 
    path('api', views.ChartData.as_view()),
    
    path('building/Aberdeen.html/', aberdeen_site, name="aberdeen_site"), 
    path('building/Ashton.html/', ashton_site, name="ashton_site"), 
    path('building/Bournemouth.html/', bournemouth_site, name="bournemouth_site"), 
    path('building/Bristol.html/', bristol_site, name="bristol_site"), 
    path('building/Bury.html/', bury_site, name="bury_site"), 
    path('building/Cardiff.html/', cardiff_site, name="cardiff_site"), 
    path('building/Cheadle.html/', cheadle_site, name="cheadle_site"), 
    path('building/Coventry.html/', coventry_site, name="coventry_site"), 
    path('building/Dudley.html/', dudley_site, name="dudley_site"), 
    path('building/Edinburgh.html/', edinburgh_site, name="edinburgh_site"), 
    path('building/Elstree.html/', elstree_site, name="elstree_site"), 
    path('building/Farnborough.html/', farnborough_site, name="farnborough_site"),  
    path('building/Glasgow.html/', glasgow_site, name="glasgow_site"), 
    path('building/HeronsReach.html/', heronsreach_site, name="heronsreach_site"), 
    path('building/Hull.html/', hull_site, name="hull_site"), 
    path('building/Hyde.html/', hyde_site, name="hyde_site"), 
    path('building/Leeds.html/', leeds_site, name="leeds_site"), 
    path('building/Liverpool_Whiston.html/', liverpool_whiston_site, name="liverpool_whiston_site"),
    path('building/Maidstone.html/', maidstone_site, name="maidstone_site"), 
    path('building/Newcastle.html/', newcastle_site, name="newcastle_site"), 
    path('building/Nottingham.html/', nottingham_site, name="nottingham_site"), 
    path('building/Portsmouth.html/', portsmouth_site, name="portsmouth_site"), 
    path('building/Solihull.html/', solihull_site, name="solihull_site"),
    path('building/SouthLeeds.html/', southleeds_site, name="southleeds_site"),
    path('building/StDavids.html/', stdavids_site, name="stdavids_site"), 
    path('building/Swansea.html/', swansea_site, name="swansea_site"), 
    path('building/Swindon.html/', swindon_site, name="swindon_site"), 
    path('building/Walsall.html/', walsall_site, name="walsall_site"), 
    path('building/Warrington.html/', warrington_site, name="warrington_site"), 
    path('building/Wirral.html/', wirral_site, name="wirral_site")
]
