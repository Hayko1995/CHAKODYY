from django.urls import path
from blog.views import CreateActions, CreateRoles, CreateGroups, CreateProjects, BlogGet


urlpatterns = [
    path('actions/create', CreateActions.as_view(), name='action'),
    path('roles/create', CreateRoles.as_view(), name='roles'),
    path('groups/create', CreateGroups.as_view(), name='groups'),
    path('projects/create', CreateProjects.as_view(), name='projects'),
    path('get', BlogGet.as_view(), name='projects'),
]
