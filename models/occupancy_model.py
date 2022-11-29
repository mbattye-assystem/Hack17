# Occupancy Model

# Imports
import numpy as np
from random import randint
import matplotlib.pyplot as plt
from functions.general_functions import *
from io_data.sql_calls import OfficeConfiguration, OccupancyOptions

def x():
    pass

# class Levels:
#     def __init__(self, level):
#         self.level = level
#     def populate_level(n):
#         levels = {}
#         perc_left = 100
#         split = perc_left/n
#         init = 10
#         buff = 3

#         while perc_left-(split+buff) > 0:
#             for x in range(1, n):
#                 if x==1:
#                     levels[f"level{x}"] = {"occupants":randint(0,100), "emissions_split":None}
#                     perc_left-=init
#                 else:
#                     emissions = randint(split-buff, split+buff)
#                     levels[f"level{x}"] = {"occupants":randint(0,100), "emissions_split":None}
#                     perc_left-=emissions
        

# class Building:
#     """
#     Create a building class with levels (floors starting at 0)
#     """
#     def __init__(self):
#         self.levels = {}
#         self.occupancy = 0
#         self.num_levels = OfficeConfiguration.number_of_floors(self)
#         self.office_space = 0

#     def total_occupancy(self):
        
#         # total_desks = OfficeConfiguration.total_desks
#         print(self.num_levels)
#         # total_desks = self.levels*100
#         # print(total_desks)
#         # table = 'PUBLIC."London_Office_Elec_and_Gas_kwh"'
#         # x = energy_normaliser(table)
#         # MONTH = 0
#         # occupancy = perc_occ(x, MONTH, total_desks)

#         # return occupancy

#     def init_levels(self):
#         for x in range(1, self.num_levels):
#             levels = Levels(x)