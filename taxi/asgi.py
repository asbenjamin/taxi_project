"""
ASGI config for taxi project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from django.urls import path
from trips.consumers import TaxiConsumer

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from taxi.middleware import TokenAuthMiddlewareStack # new

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taxi.settings')

django_asgi_application = get_asgi_application() # var modified

application = ProtocolTypeRouter({
    'http': django_asgi_application,

    'websocket': TokenAuthMiddlewareStack(  # changed
        URLRouter([
            path('taxi/', TaxiConsumer.as_asgi()),
        ])
    ),
})
