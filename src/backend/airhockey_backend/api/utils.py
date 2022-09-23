from aiohttp import web

from api.constants import UrlPatterns, METHOD_RESOLVER


class RouterRegistryService:
    """
    Class for basic application routes configuration.
    """

    def __init__(self, app: web.Application) -> None:
        """
        Initialize class with web application.
        """
        # TODO: write some list of all created routes and logger for it
        self.app = app

    def register_routes(self, patterns: UrlPatterns) -> list[web.AbstractRoute] | None:
        """
        Add package routes to your web application.

        Returns: list[aiohttp.web.AbstractRoute] | None
            List of added routes
        """
        return self.app.add_routes(
            METHOD_RESOLVER[p.method](p.url, p.view) for p in patterns
        )
