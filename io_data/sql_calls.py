# SQL Calls

# Imports
import psycopg2
import pandas as pd

def sql_connect():

    conn = psycopg2.connect(
        host="db.bit.io",
        database="wilkinsonc2/challenge13",
        user="wilkinsonc2",
        password="v2_3w8Fx_6xftS8bLJ2nfdWmbdZAc55b")

    # cursor = conn.cursor()
    # cursor.execute(f'SELECT * FROM {table}')

    # for row in cursor:
    #     print('row = %r' % (row,))
    return conn

def sql_to_df(table):
 
    conn = sql_connect()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {table}')
    df = pd.DataFrame(cursor.fetchall())
    print([desc[0] for desc in cursor.description])
    df.columns = [desc[0] for desc in cursor.description]

    return df

def office_configuration():
    table = "PUBLIC.office_configuration"
    df = sql_to_df(table)
    last_row = df.iloc[-1]
    return last_row

def occupancy_options(office_id):
    table = "PUBLIC.occupancy_options"
    df = sql_to_df(table)
    df = df[df['office_id']==office_id]

    return df

# class OfficeConfiguration:

#     def __init__(self, office_id, number_of_floors, total_desks, office_space):
#         self.office_id = df['office_id']
#         self.number_of_floors = df['number_of_floors']
#         self.total_desks = 0
#         self.office_space = 0


#     def number_of_floors(self):
#         self.number_of_floors = self.df['number_of_floors'][-1]
#         print(self.number_of_floors)
#         return self.number_of_floors
#     # def total_desks(self):
#     #     self.df['total_desks']
#     # def office_space(self):
#     #     self.df['office_space']

# class OccupancyOptions:

#     def __init__(self) -> None:
#         pass

#     table = 'PUBLIC."occupancy_options"'
#     df = sql_to_df(table)
#     def year(self):
#         self.df['year']
#     def month(self):
#         self.df['month']
#     def office_id(self):
#         self.df['office_id']
#     def which_floor(self):
#         self.df['which_floor']
#     def people_per_floor(self):
#         self.df['people_per_floor']


