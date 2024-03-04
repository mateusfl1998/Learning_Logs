from typing import Any
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Topic,Entry
from .forms import EntryForm
from django.urls import reverse_lazy

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
    success_url = reverse_lazy('topics_list')
    # def get_success_url(self):
    #     topic_id = self.object.id
    #     if topic_id:
    #         return reverse_lazy('topic_detail' 'topic_id')
    #     else:
    #         pass

class UpdateTopicView(UpdateView):
    model = Topic
    fields = ['text']
    template_name = 'update_topic.html'
    success_url = '/topics'

class DeleteTopicView(DeleteView):
    model = Topic
    template_name = 'delete_view.html'  
    success_url = '/topics'
    
   

class EntryCreateView(CreateView):
    model = Entry
    form_class = EntryForm
    template_name = 'create_new_entry.html'

    def form_valid(self, form):
        topic_id = self.kwargs['pk']
        topic = Topic.objects.get(id=topic_id)
        form.instance.topic = topic
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        topic_id = self.kwargs['pk']
        topic = Topic.objects.get(id=topic_id)
        context["topic"] = topic
        return context
    
    def get_success_url(self):
        topic_id = self.object.topic.id
        if topic_id:
            return reverse_lazy('topic_detail',kwargs={'pk': topic_id} ) 
        else:
            pass 

class UpdateEntryView(UpdateView):
    model = Entry
    fields = ['text']
    template_name = 'update_entry.html'
    success_url = reverse_lazy('topics_list')

    def get_success_url(self):
        topic_id = self.object.topic.id
        if topic_id:
            return reverse_lazy('topic_detail', kwargs={'pk': topic_id})
        else:
            # Lógica de fallback, caso o topic_id não esteja na sessão
            pass

class EntryDeleteView(DeleteView):
    model = Entry
    template_name = 'entry_delete.html'
    fields = ['text']

    def get_success_url(self):
        topic_id = self.object.topic.id
        if topic_id:
            return reverse_lazy('topic_detail', kwargs={'pk': topic_id})
        else:
            pass
        