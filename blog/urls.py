from django.urls import path
from . import views as v

app_name = 'blog'

urlpatterns = [
    path('home/',v.Post_List_View.as_view(),name='post_list'),
    path('about/',v.About_View.as_view(),name='about'),
    path('post/<int:pk>/',v.Post_Detail_View.as_view(),name='post_detail'),
    path('post/new/',v.Post_Create_View.as_view(),name='post_new'),
    path('post/<int:pk>/update/',v.Post_Update_View.as_view(),name='post_update'),
    path('post/<int:pk>/delete/',v.Post_Delete_View.as_view(),name='post_delete'),
    path('draft/',v.Draft_List_View.as_view(),name='post_draft_list'),
    path('post/<int:pk>/comment/',v.add_comment_to_post,name='add_comment_to_post'),
    path('comment/<int:pk>/approve/',v.comment_approve,name='comment_approve'),
    path('comment/<int:pk>/remove/',v.comment_remove,name='comment_remove'),
    path('post/<int:pk>/publish/',v.post_publish,name='post_publish'),
]