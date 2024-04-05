from django.urls import path
from task_manager.task import views

urlpatterns = [
        path(
            '',
            views.TaskListView.as_view(),
            name='task_list'
            ),
        path(
            '<int:pk>',
            views.TaskView.as_view(),
            name='task_detail'
            ),
        path(
            'create/',
            views.TaskCreateView.as_view(),
            name='task_create'
            ),
        path(
            '<int:pk>/update/',
            views.TaskUpdateView.as_view(),
            name='task_update'
            ),
        path(
            '<int:pk>/delete/',
            views.TaskDeleteView.as_view(),
            name='task_delete'
            ),
        ]
