from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from manager.models import *

get_object_or_404(Person, id=20)


class WorkerListView(TemplateView):
  template_name = "worker_list.html"

  def get(self, request, *args, **kwargs):
    context = super(WorkerListView, self).get_conztext_data(**kwargs)
    workers = Worker.objects.all()
    context['workers'] = workers
    return render(self.request, self.template_name, context)



