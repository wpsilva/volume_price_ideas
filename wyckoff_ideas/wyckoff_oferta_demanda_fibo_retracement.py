from wyckoff_ideas.wyckoff_oferta_demanda import WyckoffOfertaDemanda
from indicadores.indicador_fibo_retracement import IndicadorFiboRetracement

class WyckoffOfertaDemandaFiboRetracement(WyckoffOfertaDemanda):

    def __init__(self, df_OHLC):
        self.df_OHLC = df_OHLC.copy()
        self.fibo = IndicadorFiboRetracement(self.df_OHLC)

    def generate_signals(self):
        self.fibo_levels = self.fibo.calcular()
        self.df_OHLC['Signal'] = 0

        for level in self.fibo_levels.columns:
            mask = self.df_OHLC['Close'].between(self.fibo_levels[level] - 0.1 * self.fibo_levels[level], self.fibo_levels[level] + 0.1 * self.fibo_levels[level])
            
            if level in ['23.6%', '38.2%']:  # Suporte
                self.df_OHLC.loc[mask, 'Signal'] = 1
            elif level in ['61.8%', '100%']:  # Resistência
                self.df_OHLC.loc[mask, 'Signal'] = -1
                
        return self.df_OHLC