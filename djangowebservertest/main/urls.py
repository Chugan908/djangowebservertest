from django.urls import path

from main import views


urlpatterns = [
    path('', views.serialization_test, name = 'serialization'),
    path('database', views.single_database_test, name = 'single_database_test'),
    path('multdatabase', views.multiple_database_test, name = 'multiple_database_test'),
    path('updates', views.database_updates_view, name = 'updates'),
    path('plaintext', views.plaintext_view, name='plaintext')
]