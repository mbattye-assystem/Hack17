# CO2 model

# Imports
from io_data.sql_calls import sql_to_df, office_configuration, occupancy_options
from functions.general_functions import *


def default_co2_model():
    floors= 5
    people_per_floor = 100
    m2 = 7500
    MONTH = 0

    table = "PUBLIC.office_elec_and_gas_co2"
    df = sql_to_df(table)

    df['month'] = df['month'].map(month_map)
    df = df.groupby('month').mean().reset_index()

    co2_pp_pm = df['co2_ppm']/(people_per_floor*floors)
    co2_pf_pm = df['co2_ppm']/floors
    co2_pm2_pm = df['co2_ppm']/m2
    # co2_pm2_pm[MONTH]

    return co2_pm2_pm, co2_pf_pm, co2_pp_pm

def get_co2():

    line = office_configuration()
    office_space = line['office_space-sqm']
    co2_pm2_pm, co2_pf_pm, co2_pp_pm = default_co2_model()
    co2_pm = co2_pm2_pm*office_space
    return co2_pm

def get_office():
    line = office_configuration()
    total_desks = line['total_desks']
    num_of_floors = line['no_of_floors']
    office_id = line['office_id']
    df = occupancy_options(office_id)
    print(df)
    # g = df.groupby(['which_floor'])
    # d = g.last().sort_index().reset_index().drop_duplicates()
    # print(d)

