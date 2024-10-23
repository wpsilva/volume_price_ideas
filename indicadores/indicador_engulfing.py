from indicadores.indicador import Indicador
import numpy as np

class IndicadorEngulfing(Indicador):
    def __init__(self, df_OHLC):
        self.df_OHLC = df_OHLC.copy()        

    def calcular(self):
        bullish_engulfing = (
            (self.df_OHLC['Close'].shift(1) < self.df_OHLC['Open'].shift(1)) &
            (self.df_OHLC['Close'] > self.df_OHLC['Open']) &
            (self.df_OHLC['Close'] > self.df_OHLC['Open'].shift(1)) &
            (self.df_OHLC['Open'] < self.df_OHLC['Close'].shift(1))
        )
        self.df_OHLC['Bullish_Engulfing'] = np.where(bullish_engulfing, 1, 0)
        bearish_engulfing = (
            (self.df_OHLC['Close'].shift(1) > self.df_OHLC['Open'].shift(1)) &
            (self.df_OHLC['Close'] < self.df_OHLC['Open']) &
            (self.df_OHLC['Open'] > self.df_OHLC['Close'].shift(1)) &
            (self.df_OHLC['Close'] < self.df_OHLC['Open'].shift(1))
        )
        self.df_OHLC['Bearish_Engulfing'] = np.where(bearish_engulfing, 1, 0)

        return self.df_OHLC