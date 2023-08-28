# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/validation.ipynb.

# %% auto 0
__all__ = ['validate_format']

# %% ../nbs/validation.ipynb 2
import numpy as np

from .compat import DataFrame

# %% ../nbs/validation.ipynb 3
def validate_format(
    df: DataFrame,
    id_col: str = "unique_id",
    time_col: str = "ds",
    target_col: str = "y",
) -> None:
    """Ensure DataFrame has expected format.

    Parameters
    ----------
    df : pandas or polars DataFrame
        DataFrame with time series in long format.
    id_col : str (default='unique_id')
        Column that identifies each serie.
    time_col : str (default='ds')
        Column that identifies each timestamp.
    target_col : str (default='y')
        Column that contains the target.

    Returns
    -------
    None
    """
    # required columns
    missing_cols = sorted({id_col, time_col, target_col} - set(df.columns))
    if missing_cols:
        raise ValueError(f"The following columns are missing: {missing_cols}")

    # time col
    times_dtype = df[time_col].head(1).to_numpy().dtype
    if not (
        np.issubdtype(times_dtype, np.datetime64)
        or np.issubdtype(times_dtype, np.integer)
    ):
        raise ValueError(
            f"The time column ('{time_col}') should have either datetimes or integers, got '{times_dtype}'."
        )

    # target col
    target_dtype = df[target_col].head(1).to_numpy().dtype
    if not np.issubdtype(target_dtype, np.number):
        raise ValueError(
            f"The target column ('{target_col}') should have a numeric data type, got '{target_dtype}')"
        )
