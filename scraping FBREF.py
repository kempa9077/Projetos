import pandas as pd
import requests
import os
import time
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from dateutil import parser

URL = "https://fbref.com/pt/partidas/dcc5f94f/Flamengo-Palmeiras-2023Novembro8-Serie-A"
page = requests.get(URL)
content = page.content

soup = BeautifulSoup(content, "html.parser")


fixture = soup.find_all("div", class_="scorebox")


for simple_fixture in fixture:
    
    #Data do Jogo
    scorebox_meta = simple_fixture.find("div", class_="scorebox_meta")
    
    fixture_date_f1 = scorebox_meta.find("strong").text
    day_week, month_complete, day, year = fixture_date_f1.split()
    
    if month_complete == "Janeiro":
        month_num = 1
    elif month_complete == "Fevereiro":
        month_num = 2
    elif month_complete == "Março":
        month_num = 3
    elif month_complete == "Abril":
        month_num = 4
    elif month_complete == "Maio":
        month_num = 5
    elif month_complete == "Junho":
        month_num = 6
    elif month_complete == "Julho":
        month_num = 7
    elif month_complete == "Agosto":
        month_num = 8
    elif month_complete == "Setembro":
        month_num = 9
    elif month_complete == "Outubro":
        month_num = 10
    elif month_complete == "Novembro":
        month_num = 11
    else:
        month_num = 12
        
    day_ok = day.replace(",", "")
    fixture_date = date(int(year), int(month_num), int(day_ok))
    
    
    #Hora do Jogo
    venuetime = simple_fixture.find("span", class_="venuetime").text
    
    time_f = str(venuetime).replace(" (hora local)", "")
    time_fixture = datetime.strptime(time_f, "%H:%M").time()
    
    
    #Gols esperados
    score_xg = simple_fixture.find_all("div", class_="score_xg")
    
    home_score_xg_f = score_xg[0]
    away_score_xg_f = score_xg[1]
    
    
    #Gols
    score = simple_fixture.find_all("div", class_="score")
    
    home_score_f = score[0]
    away_score_f = score[1]
    

    #Nomes clubes
    strong = simple_fixture.find_all("strong")
    
    home_club_f = strong[0]
    away_club_f = strong[3]
    
    
    #Capitães e Técnicos
    datapoint = simple_fixture.find_all("div", class_="datapoint")

    home_manager_f = datapoint[0]
    home_captain_f = datapoint[1]
    away_manager_f = datapoint[2]
    away_captain_f = datapoint[3]
    

    #Formatação geral
    home_score_xg = home_score_xg_f.text.strip()
    away_score_xg = away_score_xg_f.text.strip()
    home_score = home_score_f.text.strip()
    away_score = away_score_f.text.strip()
    home_club = home_club_f.text.strip()
    away_club = away_club_f.text.strip()
    home_manager = home_manager_f.text.replace("Técnico:", "").strip()
    home_captain = home_captain_f.text.replace("Capitão:", "").strip()
    away_manager = away_manager_f.text.replace("Técnico:", "").strip()
    away_captain = away_captain_f.text.replace("Capitão:", "").strip()
    
    
    print(time_fixture)