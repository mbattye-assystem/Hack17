# Visualise CO2

# Imports
import matplotlib
from io_data.sql_calls import sql_to_df
import pandas as pd
pd.options.plotting.backend = "plotly"

def plot_co2():
    table = "vw_co2_optimum"
    df = sql_to_df(table)
    print(df)