from django import forms

from todo_list_app.models import Board, Status, Task, Coments


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ["title"]

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ["board", "title"]

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["status", "created_by", "title", "description", "assigned_to", "deadline", "finished_at"]


class MultiFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class ComentsForm(forms.ModelForm):


    class Meta:
        model = Coments
        fields = ["text"]