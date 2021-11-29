"""boutique_ado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# Importing views from app here:
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Define URL that will trigger say_hello function & return http response
    # Takes 3 params. 1st url, 2nd function, 3rd name
    # Empty string means no url specified
    path('', views.get_todo_list, name='get_todo_list'),
    path('add', views.add_item, name='add'),
    # the <> is how data moves from links or forms into 
    # templates and into views which expect it as a param
    path('edit/<item_id>', views.edit_item, name='edit'),
    path('toggle/<item_id>', views.toggle_item, name='toggle')
]
