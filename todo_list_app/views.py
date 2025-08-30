from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import FormMixin

from .forms import BoardForm, StatusForm, TaskForm, ComentsForm
from .models import *


# Create your views here.
class BoardListView(ListView):
    model = Board
    template_name = "todo_basics/show_board.html"
    context_object_name = "boards"

class CreateBoard(CreateView):
    model = Board
    template_name = "todo_basics/create_board.html"

    form_class = BoardForm
    success_url = reverse_lazy("BoardList")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BoardDetails(DetailView):
    model = Board
    template_name = "todo_basics/board_info.html"
    context_object_name = "board"

class CreateStatus(CreateView):
    model = Status
    template_name = "todo_basics/create_status.html"

    form_class = StatusForm
    success_url = reverse_lazy("BoardList")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["board_id"] = self.kwargs["board_id"]

        return context

class CreateTask(CreateView):
    model = Task
    template_name = "todo_basics/create_task.html"

    form_class = TaskForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["board_id"] = self.kwargs["board_id"]

        return context

    def get_success_url(self):
        board_id = self.object.status.board.id

        return reverse_lazy("board_info", kwargs = {"pk": board_id})

class TaskDetails(DetailView, FormMixin):
    model = Task
    template_name = "todo_basics/task_info.html"
    context_object_name = "task"
    form_class = ComentsForm

    def get_success_url(self):
        return reverse_lazy("task_info", kwargs={"pk": self.get_object().pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            coments = Coments.objects.create(text = form.cleaned_data["text"], task = self.get_object(), user = request.user)
            images = request.FILES.getlist("images")
            for image1 in images:
                coment_image = ComentImage.objects.create(coment = coments, image = image1)
            return redirect(self.get_success_url())
        return self.form_invalid(form)