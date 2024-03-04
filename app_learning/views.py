from typing import Any
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Topic,Entry
from .forms import EntryForm
from django.urls import reverse

def index(request):
    return render(request, 'index.html')

def topic_views_entrys(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = Entry.objects.all

class TopicsListView(ListView):  
    model = Topic
    template_name = 'topic_list.html'
    context_object_name = 'topics' 

class TopicDetailsView(DetailView):
    model = Topic
    template_name = 'topic_details.html'
    context = 'topics'
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        entries = self.object.entry_set.order_by('-date_add')
        context["entries"] = entries
        return context

class NewTopicCreateView(CreateView):
    model = Topic
    fields = ['text']
    template_name =  'create_new_topic.html'
    success_url = 'topics'

class UpdateTopicView(UpdateView):
    model = Topic
    fields = ['text']
    template_name = 'update_topic.html'
    success_url = '/topics'

class DeleteTopicView(DeleteView):
    model = Topic
    template_name = 'delete_view.html'

def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
    context = {'form':form, 'topic':topic}
    return render(request, 'new_entry.html',context)