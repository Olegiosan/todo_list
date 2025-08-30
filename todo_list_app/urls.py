from django.urls import path

from todo_list_app import views

urlpatterns = [
    path('show_board/', views.BoardListView.as_view(), name = 'BoardList'),
    path('create_board/', views.CreateBoard.as_view(), name = 'create_board'),
    path('board_details/<int:pk>/', views.BoardDetails.as_view(), name = 'board_info'),
    path('<int:board_id>/create_status/', views.CreateStatus.as_view(), name = 'create_status'),
    path('<int:board_id>/create_task/', views.CreateTask.as_view(), name = 'create_task'),
    path('task_details/<int:pk>/', views.TaskDetails.as_view(), name = "task_info")
    ]