# Zonal Statistics with Raster and Vector Data

This code performs zonal statistics on a raster dataset using a vector dataset. It uses the `rasterstats` library to calculate statistics such as mean, median, and standard deviation for each feature in the vector dataset based on the raster dataset. One of the benefits of this code is that it can read the raster and vector datasets directly from a ZIP file, without the need to extract the files first.

## Requirements

* Python 3.x
* `geopandas`
* `pandas`
* `rasterio`
* `rasterstats`

## Usage

1. Make sure you have installed the required libraries (`geopandas`, `pandas`, `rasterio`, and `rasterstats`) in your Python environment.
2. Download or clone the repository containing the code to your local machine.
3. Open a terminal or command prompt and navigate to the directory where the code is located.
4. Run the code by typing `python code.py`, replacing `code.py` with the name of the Python script.

### Running the Code

To run the code, follow these steps:

1. Open a terminal or command prompt.
2. Run the code by typing `python code.py`, replacing `code.py` with the name of the Python script.

## Data

The code uses a raster dataset in TIFF format and a vector dataset in shapefile format. The raster dataset is named `FUSION_DEC_2154.tif`, and the vector dataset is named `couches_projets.shp`. Both datasets are located in a ZIP file named `projets.zip`.

## License

This code is released under the MIT License.