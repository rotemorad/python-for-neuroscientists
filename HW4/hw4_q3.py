import pathlib

import pandas as pd


def read_data(fname: pathlib.Path) -> pd.DataFrame:
    file = pathlib.Path(str(fname))
    if not file.exists():
        raise FileNotFoundError(f"File {file} doesn't exist.")
    return pd.read_csv(file)


def common_complaint(fname: pathlib.Path):
    """Finds and returns the most common complaint as (complaint_name, num).

    Parameters
    ----------
    fname : pathlib.Path
        Filename for the NYC data.

    Returns
    -------
    common_complaint : tuple
        (Complaint name, number of occasions)
    """
    data = read_data(fname)
    complaints = pd.Series(data['Complaint Type'].value_counts())
    return complaints.idxmax(), complaints.max()


def parking_borough(fname: pathlib.Path) -> str:
    """Finds and returns the name of the NYC borough that has the
    most complaints of type 'Illegal Parking'.

    Parameters
    ----------
    fname : pathlib.Path
        Filename for the NYC data.

    Returns
    -------
    borough_name : str
        Name of the relevant NYC borough.
    """
    data = read_data(fname)
    data = data.filter(items=['City', 'Complaint Type', 'Park Borough'])
    filtered = data[data['Complaint Type'] == 'Illegal Parking']
    boroughs = pd.Series(filtered['Park Borough'].value_counts())
    return str(boroughs.idxmax())


if __name__ == '__main__':
    fname = pathlib.Path('311_service_requests.zip')
    print(common_complaint(fname))
    print(parking_borough(fname))
