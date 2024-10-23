from wyckoff_ideas.wyckoff_oferta_demanda import WyckoffOfertaDemanda
from indicadores.indicador_engulfing import IndicadorEngulfing
import numpy as np

class WyckoffOfertaDemandaEngulfing(WyckoffOfertaDemanda):

    def __init__(self, df_OHLC):
        self.df_OHLC = df_OHLC.copy()
        self.engulfing = IndicadorEngulfing(self.df_OHLC)
    
    def generate_signals(self):
        self.df_OHLC = self.engulfing.calcular()
        self.df_OHLC['Signal'] = 0
        
        self.df_OHLC['Signal'] = np.where(self.df_OHLC['Bullish_Engulfing'].shift(1) == 1, 1, self.df_OHLC['Signal'])
        self.df_OHLC['Signal'] = np.where(self.df_OHLC['Bearish_Engulfing'].shift(1) == 1, -1, self.df_OHLC['Signal'])

        return self.df_OHLC