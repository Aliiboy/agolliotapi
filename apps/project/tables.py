from django.utils.translation import gettext_lazy as _
from django_tables2 import Column, TemplateColumn

from apps.project.models import Project
from core.tables import AppTable


class ProjectTable(AppTable):
    number = Column(
        verbose_name=_("Number"),
        attrs={
            "th": {"class": "p-4"},
            "td": {
                "class": "p-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
            },
        },
    )
    name = Column(
        verbose_name=_("Nom"),
        attrs={
            "th": {"class": "p-4"},
            "td": {"class": "p-4"},
        },
    )
    description = Column(
        verbose_name=_("Description"),
        attrs={
            "th": {"class": "p-4"},
            "td": {"class": "p-4"},
        },
    )
    created_at = Column(
        verbose_name=_("Date de création"),
        attrs={
            "th": {"class": "p-4"},
            "td": {"class": "p-4"},
        },
    )
    updated_at = Column(
        verbose_name=_("Date de mise à jour"),
        attrs={
            "th": {"class": "p-4"},
            "td": {"class": "p-4"},
        },
    )
    actions = TemplateColumn(
        template_name="pages/projects_list/partials/project_actions.html",
        verbose_name=_("Actions"),
        attrs={
            "th": {"class": "p-4"},
            "td": {"class": "p-4 space-x-2 whitespace-nowrap"},
        },
        orderable=False,
    )

    class Meta(AppTable.Meta):
        row_attrs = {
            "class": "bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600",
        }
        model = Project
        fields = (
            "number",
            "name",
            "description",
            "created_at",
            "updated_at",
        )
        order_by = "-updated_at"
