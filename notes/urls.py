from django.urls import path,re_path

from . import views

app_name = "notes"
urlpatterns = [
    # ex: /notes/
    path("index/", views.index, name="index"),
    # ex: /notes/5/
    path("<int:article_id>/", views.article, name="article"),
    # ex: /notes/create_you/
    path('<int:article_id>/create_you/', views.create_you, name='create_you'),
    # ex: /notes/create_ai/
    path('<int:article_id>/create_ai/', views.create_ai, name='create_ai'),
    # ex: /notes/update/
    path('<int:notes_id>/update/', views.update, name='update'),
    # ex: /notes/delete/
    path('<int:notes_id>/delete/', views.delete, name='delete'),
]
