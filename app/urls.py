from django.urls import path
from app.views import (
    HomeView,
    TaskCompleteUndoView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView
)

app_name = "app"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path(
        "complete_undo_task/<int:pk>/",
        TaskCompleteUndoView.as_view(),
        name="task_complete_undo"
    ),
    # Task
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"
    ),
    path(
        "task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"
    ),
    # Tag
    path("tags/", TagListView.as_view(), name="tags"),
    path("tag/create/", TagCreateView.as_view(), name="tag-create"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),

]
