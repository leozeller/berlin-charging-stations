"""Berlin Geoheatmap - Electric Charging Stations Analysis"""

from pathlib import Path
import pandas as pd
from core import methods as cmt
from core import HelperTools as ht
from config import pdict

# Data paths
DATA_DIR = Path("datasets")
GEO_DATA_PLZ_PATH = DATA_DIR / "geodata_berlin_plz.csv"
POPULATION_PATH = DATA_DIR / "plz_einwohner.csv"
CHARGING_STATIONS_PATH = DATA_DIR / "Ladesaeulenregister_BNetzA_2025-10-23.csv"


def load_csv(path: Path, sep: str = ';', encoding: str = 'utf8') -> pd.DataFrame:
    """Load CSV file from path."""
    return pd.read_csv(path, sep=sep, encoding=encoding)


@ht.timer
def main():
    """Main: Generate Streamlit app for visualizing electric charging stations & residents in Berlin"""

    # Load data
    df_geodata = load_csv(GEO_DATA_PLZ_PATH)
    df_charging = load_csv(CHARGING_STATIONS_PATH)
    df_population = load_csv(POPULATION_PATH, sep=',')

    # Process data
    df_charging_processed = cmt.preprop_lstat(df_charging, df_geodata, pdict)
    gdf_charging_final = cmt.count_plz_occurrences(df_charging_processed)

    gdf_population_final = cmt.preprop_resid(df_population, df_geodata, pdict)

    # Launch Streamlit app
    cmt.make_streamlit_electric_Charging_resid(gdf_charging_final, gdf_population_final)


if __name__ == "__main__":
    main()