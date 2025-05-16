from django.views.generic.edit import UpdateView, CreateView
from django_tables2 import SingleTableView

from apps.project.forms import ProjectForm
from apps.project.models import Project
from apps.project.tables import ProjectTable


class ProjectListView(SingleTableView):
    model = Project
    table_class = ProjectTable
    template_name = "pages/projects_list/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all()
        return context


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "pages/projects_list/create_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Project"
        return context


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "pages/projects_list/create_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"{self.object.number} - {self.object.name}"
        return context
