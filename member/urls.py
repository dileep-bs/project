from django.conf.urls import url
from .views import getMembers,addMember,addTime

urlpatterns = [
        url('getmembers/',  getMembers.as_view(),name='get-members'),
        url('addmembers/',  addMember.as_view(),name='add-members'),
        url('addtime/',  addTime.as_view(),name='add-time'),
]