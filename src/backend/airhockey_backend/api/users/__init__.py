from . import views
from api.constants import UrlPatterns, PossibleMethods

URLS = [
    UrlPatterns(url='/users/', method=PossibleMethods.GET, view=views.get_all_users),
    UrlPatterns(url='/users/', method=PossibleMethods.POST, view=views.register_user),
]
