import pandas as pd

def check_import(data_spotify : pd.dataframe) -> bool :

    # data not empty
    if data_spotify.empty:
        print("No song downloaded, closing workflow.")
        return False

    # unique key value
    if pd.Series(data_spotify["played_at"]).is_unique:
        print("All records are unique")
    else:
         raise Exception ("Not all records are unique records, primary key is violated.")

    return
    # checks for null value

    # ensure we only have records from yesterday


    return True