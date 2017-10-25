from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status

import pandas as pd
import os

from calculationEuclidiana.views import CalculationEuclidiano

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def movies(self):
    point_search = {'coordinate_X': 1, 'coordinate_Y': 1}
    distances = get_distances(point_search)

    return HttpResponse("Movies view executed")


def get_distances(point_search):
    """Get all the distances for the point received"""
    # Read
    df_movies = pd.read_csv(PROJECT_ROOT + '/dataset-movies.csv', encoding='utf-8')
    point_dataset = dict()
    all_distances = dict()

    for index, row in df_movies.iterrows():
        point_dataset['coordinate_X'] = row['Genero']
        point_dataset['coordinate_Y'] = row['Clasificacion']
        distance = CalculationEuclidiano.calculation(point_dataset, point_search)
        all_distances[index] = [row['Resultado'], distance]

    print_dict(all_distances)
    return all_distances


def print_dict(d):
    for k, v in d.items():
        print("{}: {}".format(k, v))

#Get k number of nearest distances
def get_nearest_distances(all_distances, k):
    nearest_distances = dict()
    sorted_keys_by_distance = sorted(all_distances, key=lambda x: (all_distances[x]['distance']))
    for i in range(0, k):
        nkey = sorted_keys_by_distance[i]
        nearest_distances[nkey] = all_distances[nkey]  
    return nearest_distances

#Get most repeated result
def get_new_resultado(nearest_distances):
    count_zeros = 0;
    count_ones = 0;
    for k, v in nearest_distances.items():
        if v['resultado'] == 0:
            count_zeros += 1
        elif v['resultado'] == 1:
            count_ones += 1
    if count_zeros>count_ones:
        return 0
    else:
        return 1;
