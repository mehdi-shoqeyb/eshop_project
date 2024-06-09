from django.urls import path

from user_panel_module import views
from user_panel_module.views import EditUserProfilePage,UserPanelDashboardPage,ChangePasswordPage

urlpatterns = [
    path('',UserPanelDashboardPage.as_view(),name='user_panel_dashboard'),
    path('edit-profile',EditUserProfilePage.as_view(),name='edit_profile_page'),
    path('change-password',ChangePasswordPage.as_view(),name='change_password_page'),
    path('user-basket',views.user_basket,name='user_basket_page'),
    path('my-shoping', views.MyShopping.as_view(), name='user_shopping_page'),
    path('remove-order-detail',views.remove_order_detail,name='remove_order_detail_ajax'),
    path('change-order-detail', views.change_order_detail_count, name='change_order_detail_count_ajax'),
]