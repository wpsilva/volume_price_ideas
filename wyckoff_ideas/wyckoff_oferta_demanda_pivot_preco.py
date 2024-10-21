from wyckoff_ideas.wyckoff_oferta_demanda import WyckoffOfertaDemanda
from indicadores.indicador_pivot_preco import IndicadorPivotPreco

class WyckoffOfertaDemandaPivotPreco(WyckoffOfertaDemanda):

    def __init__(self, df_OHLC):
        self.df_OHLC = df_OHLC.copy()
        self.pivot_preco = IndicadorPivotPreco(self.df_OHLC)

    def generate_signals(self):
        self.pivots = self.pivot_preco.calcular()
        self.df_OHLC['Signal'] = 0

        for level in self.pivots.columns:
            mask = self.df_OHLC['Close'].between(self.pivots[level] - 0.1 * self.pivots[level], self.pivots[level] + 0.1 * self.pivots[level])
            
            if level in ['S1', 'S2', 'S3']:  # Suporte
                self.df_OHLC.loc[mask, 'Signal'] = 1
            elif level in ['R1', 'R2', 'R3']:  # Resistência
                self.df_OHLC.loc[mask, 'Signal'] = -1
                
        return self.df_OHLC