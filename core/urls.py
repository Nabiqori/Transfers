"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from main.views import HomePageView, ClubsView, LatestTransferView, ClubDetailsView, PlayersView, Players20View, \
    AboutView, TryoutsView, ClubsByCountry, Top150AccuratePredictions, StatsView, TransferRecords, Top50ClubExpenditure, \
    Top50ClubIncome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('clubs/', ClubsView.as_view(), name='clubs'),
    path('clubs/<int:pk>/details/', ClubDetailsView.as_view(), name='club-details'),
    path('countries/<int:pk>/clubs/', ClubsByCountry.as_view(), name='clubs-by-country'),
    path('latest-transfers/', LatestTransferView.as_view(), name='latest-transfers'),
    path('players/', PlayersView.as_view(), name='players'),
    path('players20/', Players20View.as_view(), name='players20'),
    path('about/', AboutView.as_view(), name='about'),
    path('tryouts/', TryoutsView.as_view(), name='tryouts'),
    path("150-accurate-predictions/", Top150AccuratePredictions.as_view(), name='150-accurate'),
    path("stats/", StatsView.as_view()),
    path("transfer-records/", TransferRecords.as_view()),
    path("top-50-clubs-by-expenditure-in-2021/", Top50ClubExpenditure.as_view()),
    path("top-50-clubs-by-income-in-2021/", Top50ClubIncome.as_view()),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)