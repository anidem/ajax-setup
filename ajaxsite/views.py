from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import FormView, TemplateView, CreateView, UpdateView, ListView, DetailView, View
from django.forms.models import modelformset_factory

from braces.views import CsrfExemptMixin, JSONResponseMixin, AjaxResponseMixin

from .models import Observation, Comment
from .mixins import AjaxableResponseMixin
from .forms import CommentForm

class HomeView(TemplateView):
    template_name = 'index.html'

class ObservationView(DetailView):
    model = Observation

class ObservationCreateView(CreateView):
    model = Observation
    template_name = 'make_observation.html'
    success_url = reverse_lazy('create_observation')

    def get_context_data(self, **kwargs):
        context = super(ObservationCreateView, self).get_context_data(**kwargs)
        context['commentform'] = CommentForm()
        context['observation_list'] = Observation.objects.all()
        context['comment_list'] = Comment.objects.all()
        return context      

class CommentView(DetailView):
    model = Comment
    template_name = 'comment.html'

class CommentCreateView(CsrfExemptMixin, JSONResponseMixin, AjaxResponseMixin, CreateView):
    model = Comment
    template_name = 'comment.html'
    form_class= CommentForm

    def post_ajax(self, request, *args, **kwargs):
        commentform = CommentForm(request.POST)
        commentform.save()
        return self.render_json_response(commentform.cleaned_data)
