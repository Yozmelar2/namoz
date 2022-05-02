from requests import get
from bs4 import BeautifulSoup

def NamozView(region_id):
    resp = get(f"https://islom.uz/region/{region_id}")  
    soup = BeautifulSoup(resp.text, features="lxml")
    date = soup.find('div', class_ = "date_time").text
    region_name = soup.find('div', class_ = "title_prayer").text
    bomdod = soup.find('div', id="tc1").text
    quyosh = soup.find('div', id="tc2").text
    peshin = soup.find('div', id="tc3").text
    asr = soup.find('div', id="tc4").text
    shom = soup.find('div', id="tc5").text
    xufton = soup.find('div', id="tc6").text


    times = {"date": date,"region": region_name, "bomdod": bomdod, "quyosh": quyosh, "peshin": peshin, "asr": asr, "shom": shom, "xufton": xufton}

    return times
