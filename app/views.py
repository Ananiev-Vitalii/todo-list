from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import QuerySet
from app.forms import TaskForm, TagForm
from app.models import Task, Tag


# Task
class HomeView(generic.ListView):
    model = Task
    paginate_by = 3

    def get_queryset(self) -> QuerySet[Task]:
        return Task.objects.all().order_by("is_done", "-datetime_created")


class TaskCompleteUndoView(generic.View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponseRedirect:
        return redirect(reverse_lazy("app:home"))

    def post(self, request: HttpRequest, pk: int) -> HttpResponseRedirect:
        task = Task.objects.get(pk=pk)
        action = request.POST.get("action")
        if action == "complete":
            task.is_done = True
        elif action == "undo":
            task.is_done = False
        task.save()
        return redirect(reverse_lazy("app:home"))


class TaskBaseView:
    model = Task
    success_url = reverse_lazy("app:home")


class TaskCreateView(TaskBaseView, generic.CreateView):
    form_class = TaskForm


class TaskUpdateView(TaskBaseView, generic.UpdateView):
    form_class = TaskForm


class TaskDeleteView(TaskBaseView, generic.DeleteView):
    pass


# Tag
class TagBaseView:
    model = Tag
    success_url = reverse_lazy("app:tags")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 3

    def get_queryset(self) -> QuerySet[Tag]:
        return Tag.objects.all().order_by("-id")


class TagCreateView(TagBaseView, generic.CreateView):
    form_class = TagForm


class TagUpdateView(TagBaseView, generic.UpdateView):
    form_class = TagForm


class TagDeleteView(TagBaseView, generic.DeleteView):
    pass
