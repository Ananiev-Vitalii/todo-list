from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from app.models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_class = "base-form"

        self.fields["deadline"].widget = forms.DateTimeInput(
            format="%Y-%m-%d %H:%M",
            attrs={"type": "datetime-local"}
        )

        self.helper.layout = Layout(
            Field("content", css_class="form-control"),
            Field("deadline", css_class="form-control"),
            Field("tags", css_class="form-control"),
            Submit("submit", "Submit"))


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_class = "base-form"

        self.helper.layout = Layout(
            Field("name", css_class="form-control"),
            Submit("submit", "Submit"))
