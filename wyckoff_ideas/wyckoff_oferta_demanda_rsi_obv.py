from wyckoff_ideas.wyckoff_oferta_demanda import WyckoffOfertaDemanda
from indicadores.indicador_obv import IndicadorOBV
from indicadores.indicador_rsi import IndicadorRSI

class WyckoffOfertaDemandaRSIOBV(WyckoffOfertaDemanda):

    def __init__(self, df_OHLC):
        self.df_OHLC = df_OHLC.copy()
        rsi = IndicadorRSI(self.df_OHLC)
        obv = IndicadorOBV(self.df_OHLC)
        self.df_OHLC['RSI'] = rsi.calcular()
        self.df_OHLC['OBV'] = obv.calcular()
    
    def generate_signals(self):
        conditions = [
            (self.df_OHLC['RSI'] > 70) & (self.df_OHLC['OBV'] > self.df_OHLC['OBV'].shift(1)),
            (self.df_OHLC['RSI'] < 30) & (self.df_OHLC['OBV'] < self.df_OHLC['OBV'].shift(1))
        ]
        choices = [1, -1]
        self.df_OHLC['Signal'] = 0  # Default is 0
        self.df_OHLC.loc[conditions[0], 'Signal'] = 1
        self.df_OHLC.loc[conditions[1], 'Signal'] = -1

        return self.df_OHLC
