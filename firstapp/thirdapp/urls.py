from django.urls import path
from .views import *

urlpatterns = [
    path('contact/', contact),
    path('home/', home),
    # crud operations 
    path('employees/', viewEmployees), #read R
    path('newemployee/', newEmployee), #create C
    path('insertEmployee/', insertEmployee), # insert help in create
    path('updateEmployeeForm/', updateEmployeeForm), 
    path('updateEmployee/', updateEmployee),
    path('deleteEmployee/', deleteEmployee),

    # for user login, logout, register
    path('signup/', signup),
    path('saveuser/', saveUser),
    path('login/', login),
    path('loginvalidate/', loginvalidate),
    path('logout/', logout),
]

