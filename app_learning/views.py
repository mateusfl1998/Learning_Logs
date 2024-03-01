from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Topic

def index(request):
    return render(request, 'index.html')

class TopicsListView(ListView):  
    model: Topic
    template_name = 'topics.html'
    context_object_name = 'topics' 
    queryset = Topic.objects.all()

def topicdetailsview(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_add')
    context = {'topic':topic, 'entries':entries}
    return render (request, 'topic.html', context)

class NewTopicCreateView(CreateView):
    model = Topic
    fields = ['text',]
    template_name =  'create_new_topic.html'
    success_url = 'topics'