import re


# from app.models import Earthquake

def country2countrycode(country):
    if country.lower() in ["中国", "中华人民共和国", "china"]:
        return "CHN"
    else:
        return "000"


def timestr2timecode(timestr: str):
    ## 2021-04-21 10:15:57
    p = re.compile(
        r"(?P<year>\d{,4})[-/](?P<mouth>\d{,2})[-/](?P<day>\d{,2})\s+(?P<hour>\d{,2}):(?P<minute>\d{,2}):(?P<secound>\d{,2})")
    res = p.match(timestr)
    return ''.join(res.groups())


def LAL2Positioncode(Longitude, Latitude):
    return '{0:06d}{1:06d}'.format(int(float(Longitude) * 1000), int(float(Latitude) * 1000))


def level2levelcode(levelstr):
    return '{0:02d}'.format(int(float(levelstr) * 10))


def eq_encode(country, position, time, level):
    return (country2countrycode(country) + LAL2Positioncode(*position) + timestr2timecode(time) + level2levelcode(
        level))


if __name__ == "__main__":
    print(eq_encode("中国", (10.2, 5.5), "2021-04-21 10:15:57", 3.4))
    # print(timestr2timecode("2021-04-21 10:15:57"))
    # print(LAL2Positioncode(10.2,5.5))
    # print(country2countrycode("CHINA"))
