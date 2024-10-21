from indicadores.indicador import Indicador
import pandas as pd

class IndicadorPivotPreco(Indicador):
        
    def __init__(self, df_OHLC):
        self.df_OHLC = df_OHLC.copy()

    def calcular(self):
        pivots = pd.DataFrame(index=self.df_OHLC.index)
        pivots['PP'] = (self.df_OHLC['High'] + self.df_OHLC['Low'] + self.df_OHLC['Close'] + self.df_OHLC['Open']) / 4
        pivots['R1'] = 2 * pivots['PP'] - self.df_OHLC['Low']
        pivots['S1'] = 2 * pivots['PP'] - self.df_OHLC['High']
        pivots['R2'] = pivots['PP'] + (self.df_OHLC['High'] - self.df_OHLC['Low'])
        pivots['S2'] = pivots['PP'] - (self.df_OHLC['High'] - self.df_OHLC['Low'])
        pivots['R3'] = self.df_OHLC['High'] + 2 * (pivots['PP'] - self.df_OHLC['Low'])
        pivots['S3'] = self.df_OHLC['Low'] - 2 * (self.df_OHLC['High'] - pivots['PP'])
        return pivots