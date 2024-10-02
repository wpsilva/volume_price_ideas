import pandas as pd
import yfinance as yf
from wyckoff_oferta_demanda_media_movel import WyckoffOfertaDemandaMediaMovel
from wyckoff_oferta_demanda_volume_spread import WyckoffOfertaDemandaVolumeSpread

df_OHLC = yf.download("PETR4.SA", start='2022-01-01')

wyckoff_oferta_demanda_media_movel = WyckoffOfertaDemandaMediaMovel(df_OHLC, 17, 72)
wyckoff_oferta_demanda_volume_spread = WyckoffOfertaDemandaVolumeSpread(df_OHLC)

def test(wyckoff_oferta_demanda):
    df_OHLC_with_signals = wyckoff_oferta_demanda.generate_signals()
    print(df_OHLC_with_signals[df_OHLC_with_signals["Signal"]!=0])

#test(wyckoff_oferta_demanda_media_movel)
test(wyckoff_oferta_demanda_volume_spread)