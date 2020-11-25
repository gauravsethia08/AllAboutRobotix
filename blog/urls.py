#Importing Libraries
from django.urls import path
from .views import IROSListView, TechListView, ResearchListView, IROSDetailView, ResearchDetailView, TechDetailView
from . import views

urlpatterns = [
    path('postComment', views.postComment, name='postComment'),
    path('techspresso', TechListView.as_view(), name = "techspresso"),
    path('iros2020', IROSListView.as_view(), name = "iros"),
    path('research/<int:pk>/', ResearchDetailView.as_view(), name = "research_detail"),
    path('iros2020/<int:pk>/', IROSDetailView.as_view(), name = "iros_detail"),
    path('techspresso/<int:pk>/', TechDetailView.as_view(), name = "tech_detail"),
    path('research', ResearchListView.as_view(), name = "research"),
    path('subscribe', views.subscribe, name = "subscribe")
]