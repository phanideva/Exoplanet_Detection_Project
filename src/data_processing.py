# Data Processing Module

from lightkurve import search_lightcurvefile

def run():
    print("Downloading and preprocessing light curve data for Kepler-10...")
    lc_file = search_lightcurvefile("Kepler-10", quarter=3).download()
    lc = lc_file.PDCSAP_FLUX.normalize().remove_nans().flatten(window_length=401)
    lc.to_table().write("data/kepler10_lightcurve.csv", format="csv", overwrite=True)
    print("Light curve saved to data/kepler10_lightcurve.csv")
