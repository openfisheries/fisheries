"""
Updates input CSV file (`IN`) with min and max values found in vector
layers in the database where each layer exists in a specific column
of a shared table.

(min and max for 10 km raster grids were found by manually inspecting
each layer in QGIS).

"""
import csv
import os
from sqlalchemy import func, MetaData, Table

from fisheries.fip.db import Session


DIR = os.path.dirname(os.path.abspath(__file__))
IN = os.path.join(DIR, 'vector_layers_manual.csv')
OUT = os.path.join(DIR, 'vector_layers.csv')


def get_min_max(session, table_name, column_name):
    metadata = MetaData()
    table = Table(table_name, metadata, autoload_with=session.bind)
    min_max = session.query(func.min(table.c[column_name]), func.max(table.c[column_name])).one()
    return min_max


with Session() as session, open(IN, 'r') as infile, open(OUT, 'w') as outfile:
    csv_reader = csv.reader(infile)
    csv_writer = csv.writer(outfile)
    
    for row in csv_reader:
        table_name = row[0]
        column_name = row[1]
        
        try:
            min_value, max_value = get_min_max(session, table_name, column_name)
            row[2] = str(min_value)
            row[3] = str(max_value)
        except Exception as e:
            raise ValueError(f"Error processing table {table_name}, column {column_name}: {e}")
        
        csv_writer.writerow(row)
