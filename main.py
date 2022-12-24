import pandas as pd
import numpy as np
import geoplot
import descartes
import geopandas as gpd
import matplotlib.pyplot as plt

SHAPE_FILE_PATH = "Neighborhood_Clusters/Neighborhood_Clusters.shp"
CRIME_FILE_PATH = "crime_data.csv"


def visualize_test():
    dc_map = gpd.read_file(SHAPE_FILE_PATH)
    dc_map.plot()
    plt.show()
    


if __name__ == '__main__':
    print("main test")
    visualize_test()