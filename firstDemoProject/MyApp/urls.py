from django.contrib import admin
from django.urls import path
from MyApp import views

# As more and more projects/apps are being added the main urls.py file will become crowded and difficult to maintain
# hence the urls are kept specific to individual apps

app_name = 'MyApp'   #Adding Namespace for the app URL
urlpatterns = [
    path('index/', views.index, name='index'), # Defining Custom URL - giving access to the index view created
    path('', views.index, name='index'), # Associating view to Homepage instead of custom URL

    # adding <> synmoblize generation of dynamic URL :- e.g book/2,
    # Then specify the type of value expected, followed by the variable name
    path('book/<int:book_id>', views.detailed_book_view, name='details'),
]
