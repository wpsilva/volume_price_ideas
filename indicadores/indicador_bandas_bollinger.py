from indicadores.indicador import Indicador

class IndicadorBandasBollinger(Indicador):
    def __init__(self, df_OHLC, window=17, num_std=2):
        self.df_OHLC = df_OHLC.copy()
        self.window = window
        self.num_std = num_std

    def calcular(self):
        self.df_OHLC['SMA'] = self.df_OHLC['Close'].rolling(window=self.window).mean()
        self.df_OHLC['Banda Superior'] = self.df_OHLC['SMA'] + (self.df_OHLC['Close'].rolling(window=self.window).std() * self.num_std)
        self.df_OHLC['Banda Inferior'] = self.df_OHLC['SMA'] - (self.df_OHLC['Close'].rolling(window=self.window).std() * self.num_std)
        return self.df_OHLC