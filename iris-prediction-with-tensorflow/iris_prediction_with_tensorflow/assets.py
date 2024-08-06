from dagster_deltalake import LocalConfig
from dagster_deltalake_pandas import DeltaLakePandasIOManager

import pandas as pd

from dagster import asset
from dagster import Definitions


@asset
def iris_dataset() -> pd.DataFrame:
    return pd.read_csv(
        "https://docs.dagster.io/assets/iris.csv",
        names=[
            "sepal_length_cm",
            "sepal_width_cm",
            "petal_length_cm",
            "petal_width_cm",
            "species",
        ],
    )


@asset
def iris_cleaned(iris_dataset: pd.DataFrame) -> pd.DataFrame:
    return iris_dataset.dropna().drop_duplicates()


defs = Definitions(
    assets=[iris_dataset],
    resources={
        "io_manager": DeltaLakePandasIOManager(
            root_uri="data/iris",  # required
            storage_options=LocalConfig(),  # required
            schema="iris",  # optional, defaults to "public"
        )
    },
)
