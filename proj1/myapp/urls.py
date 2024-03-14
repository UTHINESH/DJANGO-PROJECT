from django.urls import path
from . import views

urlpatterns=[
    path('',views.myapp,name=""),
    
    path('prod_details/<int:id>',views.prod_details,name='product_details'),

    # path('image/<int:id>',views.profile,name='image'),


#------------------CRUD operetions-----------------------#

    # CREATE USER

    path('create-user',views.createUser,name='create-user'),
    
    # UDATE USER

    path('update-user/<int:pk>/',views.updateUser,name='update-user'),
    
    # DETETE USER
    
    path('delete-user/<int:pk>/',views.deleteUser,name='delete-user'),


# ----------------DJANGO ADMIN USER OPERATIONS-------------------------#


    # REGISTER A USER

    path('register',views.register,name='register'),

    #LOGIN  A USER

    path('my-login',views.my_login,name='my-login'),

    # DASHBOARD PAGE

    path('dashboard',views.dashboard,name='dashboard'),

    # LOGOUT A USER

    path('usr-logout',views.user_logout,name='user-logout'),

]

