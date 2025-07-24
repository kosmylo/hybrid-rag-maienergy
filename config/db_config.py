OPENSEARCH_INDEX_CONFIG = {
    # Textual datasets
    "arxiv-articles": ["title", "url", "document_type", "chunk_id", "text_chunk"],
    "gov-articles": ["title", "url", "document_type", "chunk_id", "text_chunk"],
    "news-articles": ["title", "url", "document_type", "publishedAt", "source", "chunk_id", "text_chunk"],
    "wiki-articles": ["title", "url", "document_type", "categories", "chunk_id", "text_chunk"],
    
    # Numerical datasets
    "building-stock": ["Domain", "Category", "Subject", "Measurement", "Country", "Unit", "Reference_year", "Value", "URL", "Description"],
    "electricity-prices": ["freq", "product", "nrg_cons", "unit", "tax", "currency", "country", "period", "year", "value", "URL", "dataset_name", "description"],
    "energy-efficiency-indicators": ["freq", "nrg_bal", "unit", "country", "period", "year", "value", "URL", "dataset_name", "description"],
    "energy-import-dependency": ["freq", "siec", "unit", "country", "period", "year", "value", "URL", "dataset_name", "description"],
    "energy-intensity-economy": ["freq", "nrg_bal", "unit", "country", "period", "year", "value", "URL", "dataset_name", "description"],
    "energy-environmental-performance": ["Domain", "Category", "Subject", "Measurement", "Country", "Unit", "Reference_year", "Value", "URL", "Description"],
    "final-energy-consumption-households-per-capita": ["freq", "unit", "country", "period", "year", "value", "URL", "dataset_name", "description"],
    "financial-performance": ["Domain", "Category", "Subject", "Measurement", "Country", "Unit", "Reference_year", "Value", "URL", "Description"],
    "gas-prices": ["freq", "product", "nrg_cons", "unit", "tax", "currency", "country", "period", "year", "value", "URL", "dataset_name", "description"],
    "gdp": ["freq", "na_item", "unit", "country", "period", "year", "value", "URL", "dataset_name", "description"],
    "households-number": ["freq", "agechild", "n_child", "hhcomp", "unit", "country", "period", "year", "value", "URL", "dataset_name", "description"],
    "inability-to-keep-home-warm": ["freq", "hhtyp", "incgrp", "unit", "country", "period", "year", "value", "URL", "dataset_name", "description"],
    "population": ["freq", "age", "sex", "unit", "country", "period", "year", "value", "URL", "dataset_name", "description"],
    "reference-buildings": ["Domain", "Category", "Subject", "Measurement", "Country", "Unit", "Reference_year", "Value", "URL", "Description"],
    "renewable-energy-share": ["freq", "nrg_bal", "unit", "country", "period", "year", "value", "URL", "dataset_name", "description"],
    "social-performance": ["Domain", "Category", "Subject", "Measurement", "Country", "Unit", "Reference_year", "Value", "URL", "Description"]
}

MILVUS_COLLECTION_CONFIG = {
    "copernicus_images": ["id", "title", "url", "categories", "dataset", "country", "region"],
    "eprel_images": ["id", "title", "url", "categories", "dataset", "subcategory"],
    "inria_images": ["id", "filename", "city", "country", "url", "dataset", "resolution", "image_size"],
    "irf_images": ["id", "filename", "url", "dataset", "resolution"],
    "wikimedia_images": ["id", "title", "url", "categories", "dataset", "subcategory"],
    "wikipedia_images": ["id", "title", "url", "caption", "dataset", "resolution"]
}

NEO4J_NODE_CONFIG = {
    "cordis": {
        "Project": ["title", "acronym", "objective", "frameworkProgramme"],
        "Organization": ["name", "shortName", "country", "activityType"],
        "Topic": ["title"],
        "LegalBasis": ["title"]
    },
    "gridkit": {
        "GridNode": ["name", "type", "operator", "country"]
    },
    "osm": {
        "ChargingStation": ["name", "operator", "country", "capacity", "socket_types"],
        "PowerPlant": ["name", "operator", "country", "source", "method", "capacity"],
        "SolarFarm": ["operator", "country", "source", "method", "capacity"],
        "WindTurbine": ["manufacturer", "model", "operator", "country", "capacity", "rotor_diameter"],
        "Substation": ["country"],
        "TransmissionLine": ["name", "operator", "country", "voltage"]
    },
    "powerplants": {
        "PowerPlant": ["plant_name", "fuel_type", "capacity_mw", "source"],
        "Country": ["country_iso"],
        "Owner": ["name"],
        "FuelType": ["type"]
    },
    "tso_network": {
        "TSO": ["country", "area_code"]
    }
}