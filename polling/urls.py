from django.urls import path
from polling.views import PollListView, detail_view

urlpatterns = [
    path('', PollListView().as_view(), name="poll_index"),
    path('polls/<int:poll_id>/', detail_view, name="poll_detail"),
]
