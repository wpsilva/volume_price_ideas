import pandas as pd
from wyckoff_oferta_demanda import WyckoffOfertaDemanda

class WyckoffOfertaDemandaVolumeSpread(WyckoffOfertaDemanda):
    def __init__(self, df_OHLC):
        self.df_OHLC = df_OHLC.copy()
        self.df_OHLC['Spread'] = self.df_OHLC['High'] - self.df_OHLC['Low']
        self.df_OHLC['Volume_MA'] = self.df_OHLC['Volume'].rolling(window=20).mean()
        self.df_OHLC['Signal'] = 0

    def generate_signals(self):
        for i in range(1, len(self.df_OHLC)):
            if self.df_OHLC['Volume'].iloc[i] > self.df_OHLC['Volume_MA'].iloc[i] and self.df_OHLC['Spread'].iloc[i] > self.df_OHLC['Spread'].rolling(window=20).mean().iloc[i]:
                self.df_OHLC.at[self.df_OHLC.index[i], 'Signal'] = 1
            elif self.df_OHLC['Volume'].iloc[i] < self.df_OHLC['Volume_MA'].iloc[i] and self.df_OHLC['Spread'].iloc[i] < self.df_OHLC['Spread'].rolling(window=20).mean().iloc[i]:
                self.df_OHLC.at[self.df_OHLC.index[i], 'Signal'] = -1
            else:
                self.df_OHLC.at[self.df_OHLC.index[i], 'Signal'] = 0
        return self.df_OHLC