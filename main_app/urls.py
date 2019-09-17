from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('profile/<int:user_id>', views.user_profile, name='user_profile'),
    path('portfolio/', views.PortfolioPage.as_view(), name='portfolio'),
    path('portfolio/<int:pk>/', views.PortfolioDetail.as_view(), name='portfolio_detail'),
    path('portfolio/create/', views.PortfolioCreate.as_view(), name='portfolio_create'),
    path('portfolio/<int:pk>/update/', views.PortfolioUpdate.as_view(), name='portfolio_update'),
    path('portfolio/<int:portfolio_id>/add_photo/', views.portfolio_add_photo, name='portfolio_add_photo'),
    path('portfolio/<int:portfolio_id>/delete_photo/', views.portfolio_delete_photo, name='portfolio_delete_photo'),
    path('portfolio/<int:portfolio_id>/assoc_project/<int:project_id>/', views.assoc_project, name='assoc_project'),
    path('portfolio/<int:portfolio_id>/unassoc_project/<int:project_id>/', views.unassoc_project, name='unassoc_project'),
    path('projects/', views.ProjectList.as_view(), name='projects_index'),
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name='projects_detail'),
    path('projects/create/', views.ProjectCreate.as_view(), name='projects_create'),
    path('projects/<int:pk>/update/', views.ProjectUpdate.as_view(), name='projects_update'),
    path('projects/<int:pk>/delete/', views.ProjectDelete.as_view(), name='projects_delete'),
    path('accounts/signup', views.signup, name='signup')

]