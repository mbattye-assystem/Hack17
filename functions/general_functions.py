# Occupancy Functions

# Imports
from io_data.sql_calls import sql_to_df
from sklearn.preprocessing import Normalizer

#Dicts

month_map = {'Jan': 1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}

# Conversions

def elec_to_co2(elec):
    co2 = elec*0.193    # kwh of electricity to kg of CO2
    return co2

def gas_to_co2(gas):
    pass

def perc_occ(inp,month, total_emp):
    perc_occ = inp[0][month]*total_emp
    return perc_occ


# Energy

def energy_limits(table):

    df = sql_to_df(table)
    elec = df['Electricity (kWh)']
    max, min = df['Electricity (kWh)'].max(), df['Electricity (kWh)'].min()

    return max, min

def energy_normaliser(table):

    df = sql_to_df(table)
    df['month'] = df['month'].map(month_map)
    df = df.groupby('month').mean().reset_index()
    # elec = list(df['Electricity (kWh)'].sort_values())
    # elec = [pair for pair in enumerate(elec)]
    x = df.month
    X = df['Electricity (kWh)']
    transformer = Normalizer().fit([X])
    y = transformer.transform([X])

    # plt.scatter(x,y)
    # plt.show()

    return y