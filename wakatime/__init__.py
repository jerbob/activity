"""Constants and utilities for use in the script."""

from typing import Optional

from os import getenv


USER: Optional[str] = getenv("WAKATIME_USER")

if USER is None:
    raise EnvironmentError("$WAKATIME_USER was not provided.")
