import yfinance as yf
from wyckoff_ideas.wyckoff_oferta_demanda_media_movel import WyckoffOfertaDemandaMediaMovel
from wyckoff_ideas.wyckoff_oferta_demanda_volume_spread import WyckoffOfertaDemandaVolumeSpread
from wyckoff_ideas.wyckoff_oferta_demanda_rsi_obv import WyckoffOfertaDemandaRSIOBV
from wyckoff_ideas.wyckoff_oferta_demanda_analise_horizontal import WyckoffOfertaDemandaAnaliseHorizontal
from wyckoff_ideas.wyckoff_oferta_demanda_volume_by_price import WyckoffOfertaDemandaVolumeByPrice
from wyckoff_ideas.wyckoff_oferta_demanda_bb import WyckoffOfertaDemandaBB

#df_OHLC = yf.download("BPAC11.SA", start='2022-01-01')
df_OHLC = yf.download("PETR4.SA", start='2022-01-01')

wyckoff_oferta_demanda_media_movel = WyckoffOfertaDemandaMediaMovel(df_OHLC, 17, 72)
wyckoff_oferta_demanda_volume_spread = WyckoffOfertaDemandaVolumeSpread(df_OHLC)
wyckoff_oferta_demanda_rsi_obv = WyckoffOfertaDemandaRSIOBV(df_OHLC)
wyckoff_oferta_demanda_analise_horizontal = WyckoffOfertaDemandaAnaliseHorizontal(df_OHLC)
wyckoff_oferta_demanda_volume_by_price = WyckoffOfertaDemandaVolumeByPrice(df_OHLC)
wyckoff_oferta_demanda_bb = WyckoffOfertaDemandaBB(df_OHLC)

def test(wyckoff_oferta_demanda):
    df_OHLC_with_signals = wyckoff_oferta_demanda.generate_signals()
    print(df_OHLC_with_signals[df_OHLC_with_signals["Signal"]!=0])

#test(wyckoff_oferta_demanda_media_movel)
#test(wyckoff_oferta_demanda_volume_spread)
#test(wyckoff_oferta_demanda_rsi_obv)
#test(wyckoff_oferta_demanda_analise_horizontal)
#test(wyckoff_oferta_demanda_volume_by_price)
test(wyckoff_oferta_demanda_bb)