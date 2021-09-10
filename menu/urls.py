from django.urls import path

from menu import views

urlpatterns = [
    path('', views.index, name='index'),
    path('order/', views.UserOrderView.as_view(), name='order'),
    path('order/create/', views.create_order, name='order-create'),
    path('order/<int:pk>/delete/', views.DeleteOrderView.as_view(), name='order-delete'),
    path('food/create/', views.CreateFoodOptionView.as_view(), name='food-create'),
    path('create/', views.create_menu, name='menu-create'),
    path('<int:pk>/delete', views.DeleteMenuView.as_view(), name='menu-delete'),
    path('food/list/', views.FoodOptionListView.as_view(), name='food-list'),
    path('food/<int:pk>/delete/', views.DeleteFoodOptionView.as_view(), name='food-delete'),
]