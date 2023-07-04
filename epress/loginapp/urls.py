from django.urls import path
from .views import RegisterView, LoginView, LogoutView, HomeView, SuperView #, MainView
from .views import IndexView, ContactView, ServicesView, AboutView, HotelView, HospitalView, RestaurantView, SpaView, GymView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('super/', SuperView.as_view(), name='super'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', IndexView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('services/', ServicesView.as_view(), name='services'),
    path('about/', AboutView.as_view(), name='about'),
    path('hotel/', HotelView.as_view(), name='hotel'),
    path('restaurant/', RestaurantView.as_view(), name='restaurant'),
    path('hospital/', HospitalView.as_view(), name='hospital'),
    path('spa/', SpaView.as_view(), name='spa'),
    path('gym/', GymView.as_view(), name='gym'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)