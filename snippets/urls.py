from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers


"""For Class based views"""
# urlpatterns = [
#     path('snippets/', view=views.SnippetList.as_view()),
#     path('snippets/<int:pk>/', view=views.SnippetDetail.as_view()),
#     path('users/',view=views.UserList.as_view()),
#     path('users/<int:pk>/', view=views.UserDetail.as_view()),
#     path('api-auth/', include('rest_framework.urls')),
#     path('', views.api_root),
#     path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
# ]
# urlpatterns = [
#     path('', views.api_root),
#     path('snippets/',
#         views.SnippetList.as_view(),
#         name='snippet-list'),
#     path('snippets/<int:pk>/',
#         views.SnippetDetail.as_view(),
#         name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/',
#         views.SnippetHighlight.as_view(),
#         name='snippet-highlight'),
#     path('users/',
#         views.UserList.as_view(),
#         name='user-list'),
#     path('users/<int:pk>/',
#         views.UserDetail.as_view(),
#         name='user-detail')
# ]


"""For Function based views"""
# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]


# urlpatterns = format_suffix_patterns(urlpatterns)

"""For Viewsets"""
snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
])
