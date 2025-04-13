from django.urls import path
from formatter import views

app_name = "formatter"

urlpatterns = [
    path('formatter/',views.format_query_view, name="formatter"),
    #path('',views.index, name="index")
]