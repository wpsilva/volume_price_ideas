from wyckoff_ideas.wyckoff_oferta_demanda import WyckoffOfertaDemanda
from indicadores.indicador_topo_fundo import IndicadorTopoFundo
import numpy as np

class WyckoffOfertaDemandaProjecaoImpulso(WyckoffOfertaDemanda):

    def __init__(self, df_OHLC):
        self.topo_fundo = IndicadorTopoFundo(df_OHLC)
        self.df_OHLC = self.topo_fundo.calcular()
        self.set_diff()

    def set_diff(self):
        self.df_OHLC['valor'] = self.df_OHLC['max'].combine_first(self.df_OHLC['min'])
        #self.df_OHLC['diff'] = self.df_OHLC['valor'].diff().abs()
        self.df_OHLC = self.df_OHLC.query('~valor.isna()')
        self.df_OHLC['diff_impulso'] = np.nan
        for i in range(0, len(self.df_OHLC)-1, 2):
            valor1 = self.df_OHLC['valor'].iloc[i]
            valor2 = self.df_OHLC['valor'].iloc[i+1]

            if valor1 < valor2:
                diff = valor2 - valor1
            else:
                diff = valor1 - valor2
            self.df_OHLC['diff_impulso'].iloc[i] = diff
    
    def generate_signals(self):
        self.df_OHLC['Signal'] = 0
        self.df_OHLC = self.df_OHLC.dropna(subset='diff_impulso')
        self.df_OHLC['Signal'] = np.where(self.df_OHLC['diff_impulso'] > self.df_OHLC['diff_impulso'].shift(1), 1, np.where(self.df_OHLC['diff_impulso'] < self.df_OHLC['diff_impulso'].shift(1), -1, 0))
        return self.df_OHLC