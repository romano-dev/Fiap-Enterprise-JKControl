# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 13:51:06 2022

@author: roman
"""
import pandas as pd

from Functions.helper import read_files, concat_dataframes


dict_files = read_files('Dados/Dados_Sensores/Hora_Hora/')
df = concat_dataframes(dict_files)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df.sort_index(inplace=True)
df.fillna(0, inplace=True)
