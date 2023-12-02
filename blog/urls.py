from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='PostListView'),
    path('xml/', views.listXML, name='ListXML'),
    path('rawxml/', views.rawXML,name='rawXML'),
    path("<str:isbn>/", views.post_detalle, name="post_detalle"),
]