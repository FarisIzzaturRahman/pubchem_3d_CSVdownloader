import pandas as pd
import pubchempy as pcp
import requests
import argparse


def search_pubchem(compound: str) -> int:
    """Search PubChem for a given compound and return its CID."""
    try:
        result = pcp.get_compounds(compound, 'name', record_type='3d')[0]
        return result.cid
    except (IndexError, pcp.PubChemHTTPError) as e:
        print(f"Error searching PubChem for {compound}: {e}")
        return None


def download_sdf(cid: int) -> str:
    """Download the 3D structure of a compound in SDF format from PubChem and return the SDF text."""
    try:
        url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/SDF'
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except (requests.exceptions.RequestException, pcp.PubChemHTTPError) as e:
        print(f"Error downloading SDF for CID {cid}: {e}")
        return None


def main(csv_file: str) -> None:
    """Main function that reads a CSV file of compound names, 
    searches PubChem for each compound, and downloads the 3D
    structure of each compound in SDF format."""
    # Load table data into Pandas DataFrame
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    # Loop through DataFrame and search PubChem for each compound
    cids = []
    for index, row in df.iterrows():
        compound_name = row['compound_name']
        cid = search_pubchem(compound_name)
        cids.append(cid)
    df['cid'] = cids

    # Loop through DataFrame and download the 3D structure of each compound
    for index, row in df.iterrows():
        compound_name = row['compound_name']
        cid = row['cid']
        if cid is None:
            print(f"Error: No CID found for {compound_name}")
            continue

        sdf = download_sdf(cid)
        if sdf is None:
            print(f"Error: Unable to download SDF for {compound_name}")
            continue

        try:
            with open(f'{compound_name}.sdf', 'w') as f:
                f.write(sdf)
            print(f"Downloaded SDF for {compound_name}")
        except IOError as e:
            print(f"Error saving SDF for {compound_name}: {e}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download 3D compound structures from PubChem using a CSV file of compound names.')
    parser.add_argument('csv_file', type=str, help='Path to the CSV file containing compound names in a column named "compound_name".')
    args = parser.parse_args()
    main(args.csv_file)
