"""Calculate my most used languages for the past week."""

import json
from urllib import request

from wakatime import USER


stats = json.load(
    request.urlopen(f"https://wakatime.com/api/v1/users/{USER}/stats/last_7_days")
)
print(stats["languages"])
