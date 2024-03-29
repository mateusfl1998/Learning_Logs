"""
URL configuration for learning_log project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from app_learning.views import index, EntryDeleteView, UpdateEntryView, DeleteTopicView, TopicDetailsView, TopicsListView, NewTopicCreateView, UpdateTopicView, DeleteView, EntryCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='home'),
    path('topics',TopicsListView.as_view(), name='topics_list'),
    path('topic/<int:pk>',TopicDetailsView.as_view(), name='topic_detail'),
    path('create_topic',NewTopicCreateView.as_view(), name='topic_view_create'),
    path('topic/update/<int:pk>',UpdateTopicView.as_view(), name='topic_view_update'),
    path('topic/<int:pk>/delete',DeleteTopicView.as_view(), name='topic_view_delete'),
    path('topic/<int:pk>/add_entry',EntryCreateView.as_view(), name='entry_view_create'),
    path('entry/<int:pk>/update',UpdateEntryView.as_view(), name='entry_view_update'),
    path('entry/<int:pk>/delete',EntryDeleteView.as_view(), name='entry_view_delete'),
    path('users/',include('users.urls')),
    
    
]
