# PubChem Compound Downloader
This script downloads the 3D structures of chemical compounds from PubChem using a CSV file of compound names. For each compound name in the CSV file, the script searches PubChem for the corresponding Compound ID (CID), and then downloads the 3D structure of the compound in SDF format. The SDF file is saved in the same directory as the script.

## Dependencies
The script requires the following dependencies:

* pandas
* pubchempy
* requests
* argparse

These dependencies can be installed using pip, as follows:
```
pip install pandas pubchempy requests argparse
```

## Usage
To use the script, simply run it from the command line, passing the path to the CSV file containing the compound names. The CSV file must have a column named "compound_name" containing the names of the compounds to download.
```
python pubchem_downloader.py path/to/compounds.csv
```

## Functionality
The script performs the following tasks:

Load table data into Pandas DataFrame
Loop through DataFrame and search PubChem for each compound
Loop through DataFrame and download the 3D structure of each compound
Save the SDF file for each compound in the same directory as the script


## Documentation
The script consists of the following functions:

### search_pubchem(compound: str) -> int
This function searches PubChem for a given compound and returns its CID. If the compound is not found in PubChem, it returns None.
Arguments
compound (str): The name of the compound to search for.
Returns
cid (int): The CID of the compound if it is found in PubChem, None otherwise.

### download_sdf(cid: int) -> str
This function downloads the 3D structure of a compound in SDF format from PubChem and returns the SDF text. If the download fails, it returns None.
Arguments
cid (int): The CID of the compound to download the SDF for.
Returns
sdf (str): The SDF text of the compound if the download is successful, None otherwise.

### main(csv_file: str) -> None
This function is the main function of the script. It reads a CSV file of compound names, searches PubChem for each compound, and downloads the 3D structure of each compound in SDF format.

Arguments
csv_file (str): The path to the CSV file containing the compound names in a column named "compound_name".
Returns
None.

## Error Handling
The script includes error handling to handle the following errors:

* If the CSV file is not found, the script prints an error message and returns.
* If the compound is not found in PubChem, the script prints an error message and continues to the next compound.
* If the download of the SDF file fails, the script prints an error message and continues to the next compound.
* If there is an error saving the SDF file, the script prints an error message and continues to the next compound.

### Future Improvements
Some possible future improvements for this script include:

Adding support for downloading the 2D structure of compounds in various file formats.
Adding support for downloading other types of data from PubChem, such as properties, spectra, and bioactivity data.
Adding support for downloading compounds in bulk, rather than one at a time.

### License
This script is licensed under the MIT License. See LICENSE for more information.
