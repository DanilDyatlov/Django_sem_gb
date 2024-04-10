import logging

from django.shortcuts import render

from .forms import GamesMenu
from .logic.games import GAME_TITLES, get_results

logger = logging.getLogger(__name__)


def games(request):
    context = {}
    if request.method == 'POST':
        form = GamesMenu(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            tries = form.cleaned_data['tries']
            context['title'] = GAME_TITLES[game]
            context['results'] = get_results(game, tries)
    form = GamesMenu()
    context['form'] = form
    return render(request, 's1app/games.html', context)
