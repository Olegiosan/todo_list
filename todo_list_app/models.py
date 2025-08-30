from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey, CharField, TextField, DateTimeField, ImageField


# Create your models here.
class Board(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE, related_name="boards")
    title = CharField(max_length=500)

    def __str__(self):
        return self.title

class Status(models.Model):
    board = ForeignKey(Board, on_delete=models.CASCADE, related_name="all_status")
    title = CharField(max_length=100)

    def __str__(self):
        return self.title

class Task(models.Model):
    status = ForeignKey(Status, on_delete=models.CASCADE, related_name="tasks")
    created_by = ForeignKey(User, on_delete=models.CASCADE, related_name="created_tasks")
    title = CharField(max_length=100)
    description = TextField()
    assigned_to = ForeignKey(User, on_delete=models.CASCADE, related_name="assigned_tasks")
    created_at = DateTimeField(auto_now_add=True)
    deadline = DateTimeField()
    finished_at = DateTimeField()
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Coments(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE, related_name="coments")
    task = ForeignKey(Task, on_delete=models.CASCADE, related_name="coments")
    text = TextField()
    created_at = DateTimeField(auto_now_add=True)


class ComentImage(models.Model):
    coment = ForeignKey(Coments, on_delete=models.CASCADE, related_name="images")
    image = ImageField()


