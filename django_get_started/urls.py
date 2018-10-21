"""
Definition of urls for django_get_started.
"""

from datetime import datetime
from app.forms import BootstrapAuthenticationForm
from django.urls import path, include

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    path('', include('dining_visualizer.urls'))
]
# Examples:

# Uncomment the admin/doc line below to enable admin documentation:
# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

# Uncomment the next line to enable the admin:
# url(r'^admin/', include(admin.site.urls)),
