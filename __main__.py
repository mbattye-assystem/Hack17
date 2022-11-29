# Hack 17
# Main Module

# Imports
import argparse
from io_data.api_calls import weather_month_avg
from user_interface.greenops import run_ui
from functions.general_functions import *
from models.co2_model import get_co2, get_office
from visuals.compare_co2 import plot_co2

def argparser():
    pass

def main():
    # js = weather_month_avg()
    # run_ui()

    plot_co2()

if __name__=='__main__':
    main()