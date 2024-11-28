from django.contrib import admin
from app.models import Tag, Task


class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "content", "datetime_created", "deadline", "is_done", "get_tags"
    )
    search_fields = ("content", "tags__name")
    list_filter = ("is_done", "tags")

    def get_tags(self, obj: Task) -> str:
        return ", ".join([tag.name for tag in obj.tags.all()])

    get_tags.short_description = "Tags"


admin.site.register(Tag, TagAdmin)
admin.site.register(Task, TaskAdmin)
