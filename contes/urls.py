from django.conf.urls import patterns, include, url

from lescontes import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    #url(r'^es/', views.spanishBooks, name='index'),
    #url(r'^en/', views.englishBooks, name='index'),
    # url(r'^contes/', include('contes.foo.urls')),
    url(r'^addibook', views.ajouterIbook, name='addibook'),
    url(r'^editibook/(\w+)', views.editibook, name='editibook'),
    url(r'^accounts/login/', 'django.contrib.auth.views.login'),
    url(r'^adminhome', views.adminHome, name='adminhome'),
    url(r'^deleteibook/(\w+)', views.deletebook),
    url(r'^recherche', views.recherche),
    url(r'^logout', views.logoutadmin),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   # url(r'^admin/', include(admin.site.urls)),
    url(r'^(fr|es|en)$', views.index, name='index'),
)
