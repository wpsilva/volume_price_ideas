import pandas as pd
from indicador import Indicador

class IndicadorOBV(Indicador):
    def __init__(self, df_OHLC, periodo=14):
        self.df_OHLC = df_OHLC.copy()
        self.periodo = periodo

    def calcular(self):
        obv = [0]
        for i in range(1, len(self.df_OHLC)):
            if self.df_OHLC['Close'][i] > self.df_OHLC['Close'][i-1]:
                obv.append(obv[-1] + self.df_OHLC['Volume'][i])
            elif self.df_OHLC['Close'][i] < self.df_OHLC['Close'][i-1]:
                obv.append(obv[-1] - self.df_OHLC['Volume'][i])
            else:
                obv.append(obv[-1])
        return pd.Series(obv, index=self.df_OHLC.index)