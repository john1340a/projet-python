# Zonal Statistics with Raster and Vector Data

This code performs zonal statistics on a raster dataset using a vector dataset. It uses the `rasterstats` library to calculate statistics such as mean, median, and standard deviation for each feature in the vector dataset based on the raster dataset.

## Requirements

* Python 3.x
* `geopandas`
* `pandas`
* `rasterio`
* `rasterstats`

## Usage

1. Set the working directory to the location of the code and data files.
2. Run the code to open the raster and vector datasets.
3. Check if the CRS of the raster and vector datasets are the same. If they are not, the vector dataset will be reprojected to match the CRS of the raster dataset.
4. Use the `zonal_stats` function from the `rasterstats` library to calculate statistics for each feature in the vector dataset based on the raster dataset.

## Data

The code uses a raster dataset in TIFF format and a vector dataset in shapefile format. The raster dataset is named `FUSION_DEC_2154.tif`, and the vector dataset is named `couches_projets.shp`. Both datasets are located in a ZIP file named `projets.zip`.
