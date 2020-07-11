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


def make_row(language: dict) -> str:
    """Make a HTML table row for the provided language."""
    return f"<tr><td>{ language['name'] }</td><td>{ language['text'] }</td></tr>"


print(dedent(
    f"""
    # Languages

    <table>
          { ''.join(make_row(language) for language in languages) }
    </table>
    """
))
