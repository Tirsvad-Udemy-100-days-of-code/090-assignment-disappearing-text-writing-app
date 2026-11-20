"""@file
@brief Constants of the writing app, kept in one place.
"""

## Seconds without typing after which all text is deleted.
IDLE_TIMEOUT_SECONDS: float = 5.0

## Seconds left at which the page warns the writer that the text is about to go.
WARNING_THRESHOLD_SECONDS: float = 2.0

## Milliseconds between two state requests from the browser.
POLL_INTERVAL_MILLISECONDS: int = 200

## Host and port of the local web server.
DEFAULT_HOST: str = "127.0.0.1"
DEFAULT_PORT: int = 5000
