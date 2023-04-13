from django.urls import path
from .views import GenerateAddressView, ListAddressView, RetrieveAddressView

urlpatterns = [
    path('generate_address/', GenerateAddressView.as_view(), name='generate_address'),
    path('list_address/', ListAddressView.as_view(), name='list_addresses'),
    path('retrieve_address/<int:pk>/', RetrieveAddressView.as_view(), name='retrieve_address'),
]

print("Address API urlpatterns:", urlpatterns)  