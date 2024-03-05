from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Topic,Entry, User
from .forms import EntryForm, TopicForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import request, Http404

def index(request):
    return render(request, 'index.html')

@login_required
def topic_views_entrys(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = Entry.objects.all

@method_decorator(login_required(login_url='login'), name='dispatch')
class TopicsListView(ListView):  
    template_name = 'topic_list.html'
    context_object_name = 'topics' 

    def get_queryset(self):
        topics = Topic.objects.filter(owner=self.request.user).order_by('-date_add')
        
        return topics
    
@method_decorator(login_required(login_url='login'), name='dispatch')
class TopicDetailsView(DetailView):
    model = Topic
    template_name = 'topic_details.html'
    context = 'topics'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        entries = self.object.entry_set.order_by('-date_add')
        context["entries"] = entries
        return context
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.owner != self.request.user:
            raise Http404
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

@method_decorator(login_required(login_url='login'), name='dispatch')
class NewTopicCreateView(CreateView):
    model = Topic
    form_class = TopicForm
    template_name =  'create_new_topic.html'
    success_url = reverse_lazy('topics_list')

    def form_valid(self,form):
        user_id = self.request.user.id
        form.instance.owner_id = user_id
        return super().form_valid(form)
    
    # def get_success_url(self):
    #     topic_id = self.object.id
    #     if topic_id:
    #         return reverse_lazy('topic_detail' 'topic_id')
    #     else:
    #         pass

@method_decorator(login_required(login_url='login'), name='dispatch')
class UpdateTopicView(UpdateView):
    model = Topic
    fields = ['text']
    template_name = 'update_topic.html'
    success_url = '/topics'

@method_decorator(login_required(login_url='login'), name='dispatch')
class DeleteTopicView(DeleteView):
    model = Topic
    template_name = 'delete_view.html'  
    success_url = '/topics'
    
   
@method_decorator(login_required(login_url='login'), name='dispatch')
class EntryCreateView(CreateView):
    model = Entry
    form_class = EntryForm
    template_name = 'create_new_entry.html'

    def form_valid(self, form):
        topic_id = self.kwargs['pk']
        topic = Topic.objects.get(id=topic_id)
        user_id = self.request.user.id
        form.instance.owner_id = user_id
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

@method_decorator(login_required(login_url='login'), name='dispatch')
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

@method_decorator(login_required(login_url='login'), name='dispatch')
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
        