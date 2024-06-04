from django.urls import path,include
from . import views
urlpatterns = [
   path('task/',views.Tesk,name='Teskapp'),
   path('edit/<int:id>', views.edit_tesk,name='edit_tesk'),
   path('delete/<int:id>', views.delete_tesk,name='delete_tesk'),
]