#!/usr/bin/env python3

import json
from urllib.request import urlopen
from urllib.parse import urlencode


def dest_airports(src_airport):
    url = "http://cgi.ua.flightlookup.com/routemap/service.php?"
    data = urlencode({
        "code": src_airport,
        "random": "",
        "dest": "",
        "includepartners": "false",
        "action": "nonstops",
    })
    response = urlopen(url + data).read().decode("utf8")
    parsed = json.loads(response.replace("'", "\""))
    dests = parsed["js_config_itineraryIATAs"]
    if len(dests) == 0:
        return []
    dests = set(dests.split(","))
    if src_airport in dests:
        dests.remove(src_airport)
    return sorted(dests)

if __name__ == "__main__":
    code = input("Enter airport code: ")
    print(dest_airports(code))
