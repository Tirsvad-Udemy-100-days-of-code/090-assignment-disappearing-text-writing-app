"""@file
@brief Entry point: `python -m disappearing_text` serves the app on localhost.
"""

from disappearing_text.constants import DEFAULT_HOST, DEFAULT_PORT
from disappearing_text.presentation.composition_root import create_app


def main() -> None:
    """@brief Run the web server with debug off."""
    create_app().run(host=DEFAULT_HOST, port=DEFAULT_PORT, debug=False)


if __name__ == "__main__":
    main()
