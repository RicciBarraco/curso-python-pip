import random
import mod
import read_csv
import charts
import pandas as pd

def run():
    df = pd.read_csv('./world_population.csv')
    df = df[df['Continent'] == 'Europe']

    countries = df['Country/Territory'].values
    percentages = df['World Population Percentage'].values
    
    charts.generate_pie_chart(countries, percentages)
    
    result = mod.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = mod.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'], labels, values)



if __name__ ==  '__main__':
    run()