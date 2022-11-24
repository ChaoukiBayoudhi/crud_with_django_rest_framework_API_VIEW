from . import views
from django.urls import path, re_path
# urlpatterns = [
#     re_path(r"^api/players$", views.player_list_or_add, name="player_list_or_add"),
#     re_path(r'^api/players/(?P<pk>[0-9]+)$', views.player_details_or_update_or_delete, name="player_get_or_update_or_delete"),
#     re_path(r'^api/players/agegte/(?P<pk>[0-9]+)/$', views.player_age_gte, name="player_age_greater_than"),
# ]
urlpatterns = [
    path(r'players/',views.player_list_or_add,name="player_list"),
    path(r'players/<int:pk>/',views.player_details_or_update_or_delete,name="player_get_or_update_or_delete"),
    path(r'players/agegte/<int:age_seuil>', views.player_age_gte, name="player_age_greater_than"),

]
