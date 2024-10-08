import pandas as pd
from wyckoff_ideas.wyckoff_oferta_demanda import WyckoffOfertaDemanda

class WyckoffOfertaDemandaMediaMovel(WyckoffOfertaDemanda):
    def __init__(self, df_OHLC, short_window=50, long_window=200):
        self.df_OHLC = df_OHLC.copy()
        self.short_window = short_window
        self.long_window = long_window
        self.df_OHLC['Short_MA'] = self.df_OHLC['Close'].rolling(window=self.short_window).mean()
        self.df_OHLC['Long_MA'] = self.df_OHLC['Close'].rolling(window=self.long_window).mean()
        self.df_OHLC['Signal'] = 0

    def generate_signals(self):
        for i in range(1, len(self.df_OHLC)):
            if self.df_OHLC['Short_MA'].iloc[i] > self.df_OHLC['Long_MA'].iloc[i] and self.df_OHLC['Short_MA'].iloc[i-1] <= self.df_OHLC['Long_MA'].iloc[i-1]:
                self.df_OHLC.at[self.df_OHLC.index[i], 'Signal'] = 1
            elif self.df_OHLC['Short_MA'].iloc[i] < self.df_OHLC['Long_MA'].iloc[i] and self.df_OHLC['Short_MA'].iloc[i-1] >= self.df_OHLC['Long_MA'].iloc[i-1]:
                self.df_OHLC.at[self.df_OHLC.index[i], 'Signal'] = -1
            else:
                self.df_OHLC.at[self.df_OHLC.index[i], 'Signal'] = 0
        return self.df_OHLC