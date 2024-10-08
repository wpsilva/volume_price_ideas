import pandas as pd
import numpy as np
from scipy.signal import argrelextrema
from wyckoff_oferta_demanda import WyckoffOfertaDemanda

class WyckoffOfertaDemandaAnaliseHorizontal(WyckoffOfertaDemanda):
    def __init__(self, df_OHLC):
        self.df_OHLC = df_OHLC.copy()

    def find_support_resistance(self, window=17):
        self.df_OHLC['min'] = self.df_OHLC.iloc[argrelextrema(self.df_OHLC['Close'].values, np.less_equal, order=window)[0]]['Close']
        self.df_OHLC['max'] = self.df_OHLC.iloc[argrelextrema(self.df_OHLC['Close'].values, np.greater_equal, order=window)[0]]['Close']
        
        return self.df_OHLC

    def generate_signals(self):
        self.find_support_resistance()
        self.df_OHLC['Signal'] = 0
        self.df_OHLC.loc[self.df_OHLC['max'].notnull(), 'Signal'] = -1
        self.df_OHLC.loc[self.df_OHLC['min'].notnull(), 'Signal'] = 1

        return self.df_OHLC