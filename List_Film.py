import pandas as pd
from Film import *

film_list = []

df = pd.read_csv('oscar.csv')

for _, row in df.iterrows():
    film = Film(row['ID'], row['Film'], row['Year'], row['Award'], row['Nomination'])
    film_list.append(film)
    
def addFilm():
    iD = input("ID: ")
    name = input("Name: ")
    year = input("Year: ")
    award = input("Award: ")
    nomination = input("Nomination: ")
    film = Film(iD, name, year, award, nomination)
    film_list.append(film)

def deleteFilm(iD):
    for film in film_list:
        if film.id == iD:
            film_list.pop(int(iD))
    
def update():
    update_data = {
        'ID' : [film.id for film in film_list],
        'Film' : [film.name for film in film_list],
        'Year' : [film.year for film in film_list],
        'Award' : [film.award for film in film_list],
        'Nomination' : [film.nomination for film in film_list]
    }
    
    update_df = pd.DataFrame(update_data)
    update_df.to_csv('oscar.csv', index = False)
