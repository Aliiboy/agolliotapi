from django.contrib import admin

from apps.project.models import Project


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    search_fields = ("number", "name", "description")
    list_filter = ("created_at", "updated_at")
    readonly_fields = ("id",)


admin.site.register(Project, ProjectAdmin)
