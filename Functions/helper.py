# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 14:24:09 2022

@author: roman
"""


import os
import pandas as pd

def read_files(path):
    result_dict = {}
    for file in os.listdir(path):
        result_dict[file] = pd.read_excel(f'{path}/{file}')        
        
    return result_dict


def concat_dataframes(dict_files):
    df = pd.DataFrame()
    for key, value in dict_files.items():
        df = pd.concat([df, value])
        
    return df
