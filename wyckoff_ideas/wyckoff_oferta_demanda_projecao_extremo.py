from wyckoff_ideas.wyckoff_oferta_demanda import WyckoffOfertaDemanda
from indicadores.indicador_topo_fundo import IndicadorTopoFundo
import numpy as np

class WyckoffOfertaDemandaProjecaoExtremo(WyckoffOfertaDemanda):

    def __init__(self, df_OHLC):
        self.topo_fundo = IndicadorTopoFundo(df_OHLC)
        self.df_OHLC = self.topo_fundo.calcular()
        self.set_diff()

    def set_diff(self):
        self.df_OHLC = self.df_OHLC.query('~max.isna()')
        self.df_OHLC['diff_impulso'] = np.nan
        self.df_OHLC['diff_impulso'] = abs(self.df_OHLC['max'] - self.df_OHLC['max'].shift(1))
    
    def generate_signals(self):
        self.df_OHLC['Signal'] = 0
        self.df_OHLC = self.df_OHLC.dropna(subset='diff_impulso')
        self.df_OHLC['Signal'] = np.where(self.df_OHLC['diff_impulso'] > self.df_OHLC['diff_impulso'].shift(1), 1, np.where(self.df_OHLC['diff_impulso'] < self.df_OHLC['diff_impulso'].shift(1), -1, 0))
        return self.df_OHLC