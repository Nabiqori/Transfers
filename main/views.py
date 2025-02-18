from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import *
from django.db.models import F, ExpressionWrapper, FloatField, Sum, Q
from django.db.models.functions import Abs

class HomePageView(View):
    def get(self, request):
        return render(request, "index.html")

class ClubsView(View):
    def get(self, request):
        clubs = Club.objects.all()
        context ={
            "clubs":clubs
        }
        return render(request, 'clubs.html', context)

class ClubDetailsView(View):
    def get(self, request, pk):
        club = get_object_or_404(Club, pk=pk)
        players = club.player_set.filter(club=club).order_by('-price')
        context = {
            'club':club,
            'players':players,
        }
        return render(request, "club_details.html", context)

class LatestTransferView(View):
    def get(self, request):
        transfers = Transfer.objects.order_by('-datetime')
        context = {
            'transfers':transfers,
        }
        return render(request, "latest-transfers.html", context)

class PlayersView(View):
    def get(self, request):
        players = Player.objects.order_by('-price')
        context = {
            'players':players,
        }
        return render(request, "players.html", context)

class Players20View(View):
    def get(self, request):
        players = Player.objects.filter(age__lte=20).order_by('-price')
        context = {
            'players':players,
        }
        return render(request, "players20.html", context)

class AboutView(View):
    def get(self, request):
        return render(request, "about.html")

class TryoutsView(View):
    def get(self, request):
        return render(request, "tryouts.html")

class ClubsByCountry(View):
    def get(self, request, pk):
        country = get_object_or_404(Country, pk=pk)
        clubs = country.club_set.all()
        context = {
            'country':country,
            'clubs':clubs,
        }
        return render(request, "clubs-by-country.html", context)
class Top150AccuratePredictions(View):
    def get(self,request):
        transfers = Transfer.objects.filter(price_tft__isnull=False).annotate(
            price_diff=Abs(F('price') - F('price_tft'))
        ).order_by('price_diff')
        context = {
            "transfers":transfers,
        }
        return render(request, "stats/150-accurate-predictions.html", context)

class StatsView(View):
    def get(self,request):
        return render(request,"stats.html")

class TransferRecords(View):
    def get(self,request):
        transfers = Transfer.objects.order_by('-price')[:50]
        context = {
            "transfers":transfers,
        }
        return render(request,"stats/transfer-records.html",context)

class Top50ClubExpenditure(View):
    def get(self, request):
        season = Season.objects.filter(name="21/22").first()

        if not season:
            return render(request, "error.html", {"message": "Season 21/22 not found"})

        clubs = Club.objects.annotate(
            total_expenditure=Sum(
                'club_to__price',
                filter=Q(club_to__season=season)
            )
        ).order_by('-total_expenditure')[:50]


        context = {
            'clubs': clubs,
            'season': season
        }
        return render(request, "stats/top-50-clubs-by-expenditure-in-2021.html", context)

class Top50ClubIncome(View):
    def get(self, request):
        season = Season.objects.filter(name="21/22").first()

        if not season:
            return render(request, "error.html", {"message": "Season 21/22 not found"})

        clubs = Club.objects.annotate(
            total_income=Sum(
                'club_from__price',
                filter=Q(club_from__season=season)
            )
        ).order_by('-total_income')[:50]


        context = {
            'clubs': clubs,
            'season': season
        }
        return render(request, "stats/top-50-clubs-by-income-in-2021.html", context)