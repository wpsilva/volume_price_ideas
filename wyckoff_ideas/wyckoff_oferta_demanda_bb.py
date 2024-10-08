from wyckoff_ideas.wyckoff_oferta_demanda import WyckoffOfertaDemanda
from indicadores.indicador_bandas_bollinger import IndicadorBandasBollinger

class WyckoffOfertaDemandaBB(WyckoffOfertaDemanda):

    def __init__(self, df_OHLC):
        self.df_OHLC = df_OHLC.copy()
        self.bb = IndicadorBandasBollinger(self.df_OHLC)
    
    def generate_signals(self):
        self.df_OHLC = self.bb.calcular()
        self.df_OHLC['Signal'] = 0
        self.df_OHLC.loc[self.df_OHLC['Close'] > self.df_OHLC['Banda Superior'], 'Signal'] = -1
        self.df_OHLC.loc[self.df_OHLC['Close'] < self.df_OHLC['Banda Inferior'], 'Signal'] = 1

        return self.df_OHLC
