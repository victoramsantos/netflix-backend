import os

import pandas as pd


class DatasetRepository:
    def __init__(self):
        self.__dataset_path = os.getenv("DATASET_PATH")

    def iterate_over_movies(self):
        dataset = pd.read_csv(self.__dataset_path)
        for index, row in dataset.iterrows():
            yield {
                "movieId": row["Rank"],
                "name": row["Title"],
                "gender": row["Genre"].split(','),
                "director": row["Director"],
                "description": row["Description"],
            }
