from django import forms

from .logic.games import GAME_TITLES


class GamesMenu(forms.Form):
    game = forms.ChoiceField(label='Меню игр', choices=[(k, v) for k, v in GAME_TITLES.items()],
                             widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    tries = forms.IntegerField(label='Количество попыток', min_value=1, max_value=64)