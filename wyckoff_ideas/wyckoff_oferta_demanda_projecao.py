from wyckoff_ideas.wyckoff_oferta_demanda import WyckoffOfertaDemanda
from indicadores.indicador_topo_fundo import IndicadorTopoFundo

class WyckoffOfertaDemandaProjecao(WyckoffOfertaDemanda):

    def __init__(self, df_OHLC):
        self.df_OHLC = df_OHLC.copy()
        self.topo_fundo = IndicadorTopoFundo(self.df_OHLC)
    
    def generate_signals(self):
        self.df_OHLC = self.topo_fundo.calcular()
        self.df_OHLC['Signal'] = 0
        self.df_OHLC.loc[self.df_OHLC['max'].notnull(), 'Signal'] = -1
        self.df_OHLC.loc[self.df_OHLC['min'].notnull(), 'Signal'] = 1

        return self.df_OHLC