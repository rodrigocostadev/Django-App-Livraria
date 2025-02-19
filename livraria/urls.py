from django.urls import path, include
from django.http import HttpResponse
from livraria.views import home, logout_user, register_user, book_detail, book_delete, book_add, book_update, book_search, profile_user_view, profile_user_edit, add_cart, view_cart 


urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name="register" ),
    path('book/<int:id>/', book_detail, name="book"),
    path('delete_book/<int:id>/', book_delete, name="delete_book"),
    path('add_book/', book_add, name="add_book"),
    path('update_book/<int:id>/', book_update, name="update_book"),
    path('search/', book_search, name="book_search" ),
    # path('profile_view/', profile_user_view, name="profile_view" ),
    path('profile_view/<int:id>/', profile_user_view, name="profile_view" ),
    path('profile_edit/', profile_user_edit, name="profile_edit" ),
    path('modal_cart_add/<int:book_id>/', add_cart,name='modal_add'),
    # path('<int:book_id>', add_cart,name='modal_add'),
    # path('#myModal/<int:book_id>/', add_cart,name='modal_add'),
    
    # path('modal_cart_nav/<int:book_id>/', view_cart,name='view_cart'),
    
    # path('ratings/', include('star_ratings.urls', namespace='ratings')),
    # path('sobre/', sobre)
]




