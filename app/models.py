from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Task(models.Model):
    content = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["-datetime_created", "is_done"]

    def __str__(self) -> str:
        return f"{self.content}"
