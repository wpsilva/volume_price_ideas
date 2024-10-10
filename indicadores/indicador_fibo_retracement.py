from indicadores.indicador import Indicador
import pandas as pd

class IndicadorFiboRetracement(Indicador):
    def __init__(self, df_OHLC, window=17):
        self.df_OHLC = df_OHLC.copy()
        self.window = window
    
    def calcular(self):
        fib_levels = pd.DataFrame(index=self.df_OHLC.index)
        for i in range(self.window, len(self.df_OHLC)):
            high = self.df_OHLC['Close'][i-self.window:i].max()
            low = self.df_OHLC['Close'][i-self.window:i].min()
            difference = high - low
            levels = {
                '0%': low,
                '23.6%': low + 0.236 * difference,
                '38.2%': low + 0.382 * difference,
                '50%': low + 0.5 * difference,
                '61.8%': low + 0.618 * difference,
                '100%': high
            }
            for level in levels:
                fib_levels.loc[self.df_OHLC.index[i], level] = levels[level]
        
        return fib_levels.fillna(0)