import pandas as pd

def check_import(data_spotify) -> bool :

    # data not empty
    if data_spotify.empty:
        print("No song downloaded, closing workflow.")
        return False

    # unique key value
    if pd.Series(data_spotify["played_at"]).is_unique:
        print("All records are unique")
    else:
         raise Exception ("Not all records are unique records, primary key is violated.")

    # checks for null value
    if data_spotify.isnull().values.any():
        raise Exception ("Some data have missing value, workflow terminated. Please investigate JSON file")

    return True