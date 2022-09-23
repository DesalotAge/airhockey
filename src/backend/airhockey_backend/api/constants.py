"""
Module for all stateless objects.
"""
from typing import Callable, NamedTuple

from aiohttp import web

from enum import Enum


class PossibleMethods(Enum):
    GET = 'get'
    POST = 'post'
    PUT = 'put'


METHOD_RESOLVER: [PossibleMethods, Callable] = {
    PossibleMethods.GET: web.get,
    PossibleMethods.POST: web.post,
    PossibleMethods.PUT: web.put,
}


class UrlPatterns(NamedTuple):
    url: str
    view: Callable[[web.Request], web.Response]
    method: PossibleMethods
