from django.urls import re_path
from .views import (addbook, booklist, updatebook, bookdetail)


urlpatterns = [
    re_path(r'^$', booklist, name='booklist'),
    re_path(r'^addbook/$', addbook, name='addbook'),
    re_path(r'^(?P<id>[0-9]+)/$', bookdetail, name='bookdetail'),
    re_path(r'^(?P<id>[0-9]+)/edit/$', updatebook, name='updatebook'),
]


