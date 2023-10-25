"""
This module provides functions for extracting data from url to a file path.
The data must be in CSV format.
"""
import pandas as pd


def extract(
    url: str = "https://www.basketball-reference.com/leagues/NBA_2023_per_game.html#per_game_stats",
    file_path: str = "data/nba_data.csv",
) -> str:
    """ "Extract data from url to a file path. The data must be in CSV format."""

    pd.read_html(url)[0].to_csv(file_path, index=False)

    return file_path
