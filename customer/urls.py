from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('logout_user/', views.logout_user, name='logout-user'),
	path('add_record/', views.add_record, name='add-record'),
	path('update_record/<record_id>', views.update_record, name='update-record'),
	path('delete_record/<record_id>', views.delete_record, name='delete_record'),
	path('show_record/<record_id>', views.show_record, name='show-record'),
	path('search_record/', views.search_record, name='search-record'),
	path('register_user/', views.register_user, name='register-user'),
	path('csv_record/', views.csv_record, name='csv-record'),
	path('pdf_record/', views.pdf_record, name='pdf-record'),
	path('record_list/', views.record_list, name='record-list'),

]
