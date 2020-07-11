"""Calculate my most used languages for the past week."""

import json
from urllib import request
from textwrap import dedent

from wakatime import USER


stats = json.load(
    request.urlopen(f"https://wakatime.com/api/v1/users/{USER}/stats/last_7_days")
)["data"]

languages = sorted(
    stats["languages"],
    reverse=True,
    key=lambda language: language["total_seconds"]
)


def show_language(language: dict) -> str:
    """Make a HTML table row for the provided language."""
    return f"<tr><td>{ language['name'] }</td><td>{ language['digital'] }</td></tr>"


print(dedent(
    f"""
    <table><tr><td valign="top">

    **Recent Languages:**

    <table>
    { ''.join(show_language(language) for language in languages) }
    </table>
    <a href="https://github.com/anonguy/anonguy/actions"><img src="https://github.com/anonguy/anonguy/workflows/Build%20README/badge.svg" align="center" alt="Build README"></a>
    </td><td valign="top">

    <img src="https://wakatime.com/share/@Aperture/0cd21d5d-ac4f-458d-9c71-d06f479c1297.png" />
    </td></tr></table>
    """
))
