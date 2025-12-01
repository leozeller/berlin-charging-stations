# Project Documentation

## Program Structure

### Overview
```
berlingeoheatmap_project1/
├── main.py              # Entry point - loads data and starts Streamlit app
├── config.py            # Configuration parameters (filters, settings)
├── core/
│   ├── methods.py       # Data processing pipeline functions
│   └── HelperTools.py   # Utility functions (timer decorator)
└── datasets/            # Raw data files
```

### main.py - Data Flow

1. **Load Data**
   - `load_csv()`: Generic CSV loader with configurable separator and encoding
   - Loads 3 datasets: geodata, charging stations, population

2. **Process Data**
   - `cmt.preprop_lstat()`: Cleans charging station data, filters for Berlin, merges with geodata
   - `cmt.count_plz_occurrences()`: Aggregates charging stations per PLZ
   - `cmt.preprop_resid()`: Processes population data, merges with geodata

3. **Visualize**
   - `cmt.make_streamlit_electric_Charging_resid()`: Creates interactive Streamlit app with heatmaps

### Key Components

**config.py (pdict)**
- Contains filter parameters for data preprocessing
- Defines which columns to use, region filters, etc.

**core/methods.py**
- `preprop_lstat()`: Preprocessing for charging stations
- `preprop_resid()`: Preprocessing for residents
- `count_plz_occurrences()`: Aggregation logic
- `make_streamlit_electric_Charging_resid()`: Streamlit UI creation

**core/HelperTools.py**
- `@timer`: Decorator to measure execution time

### Data Structure

**Input Files:**
1. `geodata_berlin_plz.csv`: PLZ boundaries (polygons)
2. `plz_einwohner.csv`: Population per PLZ
3. `Ladesaeulenregister_BNetzA_2025-10-23.csv`: Charging station registry

**Output:**
- GeoDataFrame with PLZ geometries + charging station counts
- GeoDataFrame with PLZ geometries + population data

## Analysis Results

### Methodology
1. Count charging stations per postal code (PLZ)
2. Normalize by population density
3. Visualize as choropleth heatmap with two layers:
   - **Charging Stations**: Distribution of existing charging infrastructure
   - **Residents**: Population density per PLZ

### Key Findings

Based on the interactive heatmap visualization:

**High Demand Areas** (High population density + Few charging stations):

**Eastern Districts:**
- **Marzahn-Hellersdorf (Northeast, red areas)**: Very high population density (35,000+ residents) with relatively few charging stations. This area shows the highest demand for additional infrastructure.
- **Lichtenberg (East)**: High residential population with insufficient charging coverage.

**Southeastern Areas:**
- **Treptow-Köpenick**: Moderate to high population, limited charging infrastructure visible.

**Analysis of Charging Stations Layer:**
- **Low station density** (105 or fewer stations): Most of Berlin shows yellow to light orange colors, indicating relatively low charging station coverage across most PLZ areas.
- **Moderate coverage** (orange areas): Some central and western districts have better infrastructure.
- **Highest concentration** (red areas, if any): Very few areas show red coloring, suggesting no single PLZ has overwhelming infrastructure.

**Analysis of Residents Layer:**
- **Highest population density** (red areas): Northeast districts (Marzahn-Hellersdorf) with 35,000+ residents per PLZ.
- **High density** (orange areas): Central, northern, and eastern districts show high residential concentration.
- **Lower density** (yellow areas): Western suburbs and peripheral areas have moderate population.

### Recommendations

**Priority 1 - Immediate Action Required:**
- **Marzahn-Hellersdorf**: Critical need for charging infrastructure expansion due to extreme population density and minimal current coverage.
- **Lichtenberg**: High-priority area for new charging stations.

**Priority 2 - Medium-term Expansion:**
- **Northern districts**: Pankow and surrounding areas show moderate demand.
- **Southern areas**: Neukölln and Treptow-Köpenick require additional stations.

**Priority 3 - Lower Priority:**
- **Western suburbs**: Already have relatively better coverage compared to population.
- **Peripheral areas**: Lower population density reduces immediate demand.

### Strategic Insights
1. **East-West Divide**: Clear pattern shows eastern districts are underserved compared to western areas.
2. **Population Concentration**: Areas with 20,000+ residents per PLZ should be prioritized for infrastructure investment.
3. **Equity Consideration**: Outer eastern districts may have lower EV adoption currently but require infrastructure to enable future adoption.

### Limitations
- Does not account for one-family houses with private charging solutions (more common in suburban areas).
- Static snapshot from October 2025, does not predict future EV adoption trends.
- No data on station utilization rates or power output (kW) distribution.
- Does not consider commuter patterns or workplace charging availability.

## Technical Details

**Libraries Used:**
- `pandas`: Data manipulation
- `geopandas`: Geospatial data handling
- `streamlit`: Web application framework
- `plotly`/`folium`: Interactive maps

