from indicadores.indicador import Indicador

class IndicadorRSI(Indicador):
    def __init__(self, df_OHLC, periodo=14):
        self.df_OHLC = df_OHLC.copy()
        self.periodo = periodo

    def calcular(self):
        delta = self.df_OHLC['Close'].diff(1)
        ganho = delta.where(delta > 0, 0)
        perda = -delta.where(delta < 0, 0)

        media_ganho = ganho.rolling(window=self.periodo, min_periods=1).mean()
        media_perda = perda.rolling(window=self.periodo, min_periods=1).mean()

        rs = media_ganho / media_perda
        rsi = 100 - (100 / (1 + rs))
        
        return rsi