from indicadores.indicador import Indicador
import numpy as np

class IndicadorDoji(Indicador):
    def __init__(self, df_OHLC):
        self.df_OHLC = df_OHLC.copy()

    def calcular(self):
        doji = (abs(self.df_OHLC['Close'] - self.df_OHLC['Open']) <= (self.df_OHLC['High'] - self.df_OHLC['Low']) * 0.1)
        self.df_OHLC['Doji'] = np.where(doji, 1, 0)
        return self.df_OHLC