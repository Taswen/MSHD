import re

# from app.models import Earthquake

def country2countrycode(country):
    if country.lower() in ["中国","中华人民共和国","china"]:
        return "CHN"
    else:
        return "000" 


def timestr2timecode(timestr:str):
    ## 2021-04-21 10:15:57
    p = re.compile(r"(?<year>\d{:4})[-/](?<mouth>\d{:2})[-/](?<day>\d{:2})\s+(?<hour>\d{:2}):(?<minute>\d{:2}):(?<secound>\d{:2})")
    res = p.findall(timestr)
    return res.group()
    # date,time = timestr.split(" ")
    # year,mouth,day = re.split("[-/]",date)
    # hour,minute,secound = re.split("[:]",time)
    # return '{0:>04s}{1:>02s}{2:>02s}{3:>02s}{4:>02s}{5:>02s}'.format(year,mouth,day,hour,minute,secound)

def LAL2Positioncode(LAL):
    pass



def level2levelcode(levelstr):
    print(float(levelstr)*10)
    s = '{0:02d}'.format( int(float(levelstr)*10))
    return s

def eqCode(country,posotion,time,level):
    pass

# def eq2code(eq:Earthquake):
    # pass


if __name__ == "__main__":
    print(country2countrycode("CHINA"))