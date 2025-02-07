import numpy as np

from pandas._typing import npt

def array_strptime(
    values: npt.NDArray[np.object_],
    fmt: str | None,
    exact: bool = True,
    errors: str = "raise",
) -> tuple[np.ndarray, np.ndarray]: ...

# first  ndarray is M8[ns], second is object ndarray of tzinfo | None
