from indicadores.indicador import Indicador
from scipy.signal import argrelextrema
import numpy as np

class IndicadorTopoFundo(Indicador):
    def __init__(self, df_OHLC, periodo=17):
        self.df_OHLC = df_OHLC
        self.periodo = periodo

    def find_support_resistance(self, window=17):
        self.df_OHLC['min'] = self.df_OHLC.iloc[argrelextrema(self.df_OHLC['Low'].values, np.less_equal, order=window, mode='wrap')[0]]['Low']
        self.df_OHLC['max'] = self.df_OHLC.iloc[argrelextrema(self.df_OHLC['High'].values, np.greater_equal, order=window, mode='wrap')[0]]['High']
        return self.df_OHLC
    
    def filter_consecutive_extremes(self):
        self.df_OHLC = self.df_OHLC.query('~min.isna() | ~max.isna()')
        for i in range(1, len(self.df_OHLC)):
            if not np.isnan(self.df_OHLC['max'].iloc[i]) and not np.isnan(self.df_OHLC['max'].iloc[i-1]):
                if self.df_OHLC['max'].iloc[i] > self.df_OHLC['max'].iloc[i-1]:
                    self.df_OHLC['max'].iloc[i-1] = np.nan
                else:
                    self.df_OHLC['max'].iloc[i] = np.nan

        for i in range(1, len(self.df_OHLC)):
            if not np.isnan(self.df_OHLC['min'].iloc[i]) and not np.isnan(self.df_OHLC['min'].iloc[i-1]):
                if self.df_OHLC['min'].iloc[i] < self.df_OHLC['min'].iloc[i-1]:
                    self.df_OHLC['min'].iloc[i-1] = np.nan
                else:
                    self.df_OHLC['min'].iloc[i] = np.nan
                    
        return self.df_OHLC


    def filter_relevant_swings(self):
        df = self.df_OHLC
        filtered_swings = []
        last_high = -np.inf
        last_low = np.inf
        high_index = None
        low_index = None

        for index, row in df.iterrows():
            if not np.isnan(row['max']):
                if row['max'] > last_high:
                    last_high = row['max']
                    high_index = index
            if not np.isnan(row['min']):
                if row['min'] < last_low:
                    last_low = row['min']
                    low_index = index

            if high_index is not None:
                filtered_swings.append((high_index, last_high, 'high'))
                high_index = None
                last_low = np.inf 
            if low_index is not None:
                filtered_swings.append((low_index, last_low, 'low'))
                low_index = None
                last_high = -np.inf

        highs = [(s[0], s[1]) for s in filtered_swings if s[2] == 'high']
        lows = [(s[0], s[1]) for s in filtered_swings if s[2] == 'low']
        high_indexes, high_values = zip(*highs) if highs else ([], [])
        low_indexes, low_values = zip(*lows) if lows else ([], [])
        
        df['max_filtered'] = np.nan
        df['min_filtered'] = np.nan
        df.loc[high_indexes, 'max_filtered'] = high_values
        df.loc[low_indexes, 'min_filtered'] = low_values

        return df
    

    def calcular(self):
        self.df_OHLC = self.find_support_resistance()
        self.df_OHLC = self.filter_consecutive_extremes()
        self.df_OHLC = self.filter_relevant_swings()
        
        return self.df_OHLC