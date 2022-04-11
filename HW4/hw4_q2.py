import pathlib

import pandas as pd


def read_data(fname: pathlib.Path) -> pd.DataFrame:
    file = pathlib.Path(str(fname))
    if not file.exists():
        raise ValueError(f"File {file} doesn't exist.")
    return pd.read_table(file)


def largest_species(fname: pathlib.Path) -> pd.Series:
    """Returns the name of the most widespread species per year.

    Parameters
    ----------
    fname : pathlib.Path
        Filename for the columnar data containing the population numbers.

    Returns
    -------
    largest_by_year : pd.Series
        Name of most common species per year
    """
    data = read_data(fname)
    index = data.pop('# year')
    final_data = data.idxmax(1).to_numpy()
    return pd.Series(final_data, index=index)


def lynxes_when_hares(fname: pathlib.Path) -> pd.Series:
    """Returns the number of lynxes when hares > foxes.

    Parameters
    ----------
    fname : pathlib.Path
        Filename for the columnar data containing the population numbers.

    Returns
    -------
    lynxes : pd.Series
        Number of lynxes when hares > foxes
    """
    data = read_data(fname)
    condition = data[data['hare'] > data['fox']]
    lynx = condition.pop('lynx').to_numpy()
    years = condition.pop('# year')
    return pd.Series(data=lynx, index=years)


def mean_animals(fname: pathlib.Path) -> pd.DataFrame:
    """Adds a column with the normalized mean number of animals in each year.

    This means that in the year with most animals, this column will have the value of 1,
    and in the rest of the years the value will be between [0, 1).

    Parameters
    ----------
    fname : pathlib.Path
        Filename for the columnar data containing the population numbers.

    Returns
    -------
    data : pd.DataFrame
        Original dataset with the new "mean_animals" column.
    """
    data = read_data(fname)
    data.pop('# year')
    data = data.assign(mean_animals=data.mean(1))
    data['mean_animals'] = (data['mean_animals'] - data['mean_animals'].min()) / (
            data['mean_animals'].max() - data['mean_animals'].min())
    return data
