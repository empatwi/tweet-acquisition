# Empatwi

## Tweet acquisition

This repository is a part of our project Empatwi. It is used to stream tweets containing certain keywords from twitter API.
All streamed data is saved into a .csv file called `raw_stream_output.csv`. We also use a Jupyter notebook script (`files/csv_treatment.ipynb`) to remove any duplicates that might occur during streaming from this raw file and save the new dataframe into a new file called `filtered_stream_output.csv`.

## Instructions

It is required to have `pip` and any virtual environment manager installed to run this script.
1. First, create your virtual environment by running `python -m venv venv` on Windows terminal.
2. Then, run `pip install -r requirements.txt` on your shell to install all dependencies.
3. To run the script, go to `twitter` folder (`cd src/twitter`) and run `python tweet_acquisition.py`.
4. You can stop streaming when desired by pressing `Ctrl+C` on your terminal.
5. A file called `raw_stream_output.csv` will be generated on `files` folder.
6. Run the `csv_treatment.ipynb` script on Jupyter notebook to remove the duplicates and generate a new dataframe.

## Developed by:
- Fabiana Masini Garcia
- Letícia Vigna Modenese Silva
