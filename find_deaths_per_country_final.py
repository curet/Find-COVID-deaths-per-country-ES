# coding=utf-8
# This program read a csv file and find the amount of death in a specific date and country

while True: # repeat the program

    #read the csv file
    import pandas as pd
    df = pd.read_csv('time_series_covid19_deaths_global.csv')
    raw_country = df[['Country/Region']]

    print("Reporte de las muertes causadas por COVID-19")

    #group dataset by Country/Region
    countries_dataset = raw_country.groupby(by="Country/Region").sum().index.tolist()
    print("\nHay información disponible de los siguientes paises: ", countries_dataset)

    #insert contry name and input validation
    country = input("\nEntre el nombre del país a buscar: ")
    while (df['Country/Region'] == country).sum() < 1:
        print("\nNo hay información sobre ", country, ". Se sugiere revisar si escribió correctamente el nombre\n")
        country = input("\nEntre el nombre del país a buscar: ")

    #insert date
    date = input("\nEntre la fecha que desea buscar --> ejemplo: 4/6/20: ")
    find = df.loc[df['Country/Region'] == country].sum()
    death_per_date = find[[date]]

    #output amount of death per country
    print("\nLa cantidad de muertes por COVID-19 hasta el ", date, "es de ", death_per_date[date])

    #program repeat statement
    repeat = input("Desea hacer otra busqueda? Y/n ")
    if repeat == 'N' or repeat == 'n':
        break
