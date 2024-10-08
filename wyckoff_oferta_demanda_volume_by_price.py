import pandas as pd
import numpy as np
from wyckoff_oferta_demanda import WyckoffOfertaDemanda

class WyckoffOfertaDemandaVolumeByPrice(WyckoffOfertaDemanda):
    
    def __init__(self, df_ohlc):
        self.df_ohlc = df_ohlc.copy()
    
    def volume_by_price(self, bins=17):
        volume_by_price = self.df_ohlc.groupby(pd.cut(self.df_ohlc['Close'], bins=bins))['Volume'].sum().reset_index()
        return volume_by_price
    
    def generate_signals(self):
        volume_by_price = self.volume_by_price()

        high_demand_threshold = volume_by_price['Volume'].quantile(0.75)
        high_offer_threshold = volume_by_price['Volume'].quantile(0.25)
        
        self.df_ohlc['Signal'] = 0

        for i in range(len(volume_by_price)):
            if volume_by_price.iloc[i]['Volume'] > high_demand_threshold:
                self.df_ohlc.loc[(self.df_ohlc['Close'] > volume_by_price.iloc[i]['Close'].left) &
                            (self.df_ohlc['Close'] <= volume_by_price.iloc[i]['Close'].right), 'Signal'] = 1
            elif volume_by_price.iloc[i]['Volume'] < high_offer_threshold:
                self.df_ohlc.loc[(self.df_ohlc['Close'] > volume_by_price.iloc[i]['Close'].left) &
                            (self.df_ohlc['Close'] <= volume_by_price.iloc[i]['Close'].right), 'Signal'] = -1
        
        return self.df_ohlc