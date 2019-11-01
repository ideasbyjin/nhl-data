import re
C = re.compile(r"\d{8}")

def validate_season(season_string):
    return C.match(season_string)