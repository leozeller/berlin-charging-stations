# Berlin Charging Stations Heatmap

Streamlit app for analyzing electric charging station demand in Berlin based on population density and existing infrastructure.

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
streamlit run main.py
```

## Project Structure
```
berlingeoheatmap_project1/
├── main.py              # Main application
├── config.py            # Configuration parameters
├── requirements.txt     # Dependencies
├── core/                # Core functionality
│   ├── methods.py       # Data processing pipeline
│   └── HelperTools.py   # Helper functions
└── datasets/            # Data files
    ├── geodata_berlin_plz.csv
    ├── plz_einwohner.csv
    └── Ladesaeulenregister_BNetzA_2025-10-23.csv
```

## Data Sources

- **Charging Stations**: [Bundesnetzagentur](https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/E-Mobilitaet/start.html)
- **Population Data**: plz_einwohner.csv
- **Geodata**: geodata_berlin_plz.csv

## Original Project

Based on assignment from: https://github.com/MathforDataScience/berlingeoheatmap_project1
