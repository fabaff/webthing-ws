"""Exceptions for WebThing WS."""


class WebThingWsError(Exception):
    """General WebThing exception occurred."""

    pass


class WebThingWsConnectionError(WebThingWsError):
    """When a connection error is encountered."""

    pass


class WebThingWsDataAvailable(WebThingWsError):
    """When no data is available."""

    pass
