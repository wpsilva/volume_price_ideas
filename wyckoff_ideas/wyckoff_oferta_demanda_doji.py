from wyckoff_ideas.wyckoff_oferta_demanda import WyckoffOfertaDemanda
from indicadores.indicador_doji import IndicadorDoji

class WyckoffOfertaDemandaDoji(WyckoffOfertaDemanda):

    def __init__(self, df_OHLC):
        self.df_OHLC = df_OHLC.copy()
        self.doji = IndicadorDoji(self.df_OHLC)
    
    def generate_signals(self):
        self.df_OHLC = self.doji.calcular()
        self.df_OHLC['Signal'] = 0

        for i in range(1, len(self.df_OHLC)):
            if self.df_OHLC['Doji'].iloc[i-1] == 1 and self.df_OHLC['Close'].iloc[i] > self.df_OHLC['Open'].iloc[i]:
                self.df_OHLC['Signal'].iloc[i] = 1

        for i in range(1, len(self.df_OHLC)):
            if self.df_OHLC['Doji'].iloc[i-1] == 1 and self.df_OHLC['Close'].iloc[i] < self.df_OHLC['Open'].iloc[i]:
                self.df_OHLC['Signal'].iloc[i] = -1
        
        return self.df_OHLC