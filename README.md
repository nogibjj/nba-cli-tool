## NBA Satistics Command Line Tool (Available on PyPi)
### By Rakeen Rouf
[![CI](https://github.com/nogibjj/nba-cli-tool/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/nba-cli-tool/actions/workflows/cicd.yml)

This project is a demonstration of a robust Command Line Interface (CLI) tool designed for effortless data handling and statistical analysis in NBA sports betting. The CLI can be easily installed using PIP, allowing users to swiftly access high-quality statistics for upcoming or past NBA basketball games. During each run, the CLI prioritizes the update of a local Sqlite Database by adding only missing information, thereby substantially enhancing processing efficiency. It subsequently identifies all scheduled games for the specified date and generates valuable statistics that can inform sound NBA sports trading choices.


## Installation

To install My CLI Tool, you can use pip:

```
pip install nba-stats-dragon
```

## Usage

To use My CLI Tool, simply run the `nbastats` command from the command line. You can pass arguments and options to the command to perform specific tasks.

Here are some examples of how to use My CLI Tool:

```
# Display help information
nbastats --help
```

```
# Get NBA Stats for 2022-11-16 using matches from the 2022-23 Season
# Scaled statistics were calculated using game between 2022-10-01 & 2022-03-30
nbastats -d 2022-11-16 -hsd 2022-10-01 -hed 2023-03-30
```

![Alt text](https://user-images.githubusercontent.com/36940292/278879474-4f1af56e-23ba-4f82-a95b-d20a27643e20.png)
![Alt text](https://user-images.githubusercontent.com/36940292/278879511-eac21c77-1cd7-43d6-a769-8352b70d5b09.png)
![Alt text](https://user-images.githubusercontent.com/36940292/278879535-15f0ef59-3a55-4cba-ae26-7c8e2c0eb454.png)

## Options

Here are the available options for My CLI Tool:

- `--help`: Display help information
- `-d`, `--date` [%Y-%m-%d]: Date to run Statistic for. Will run stats for all games on --date.
- `-hsd`, `--historical_start_date` [%Y-%m-%d]: Start date for historical game day (used in scaled calculations)
- `-hed`, `--historical_end_date` [%Y-%m-%d]: End date for historical game day (used in scaled calculations)
- `-s`, `--season` TEXT: Season to run the statistics for (YYYY-YY)


## Result Tables

Here are the available statistics for the nba-stats-dragon:

- `Head to Head Games`: Table of all games played so far in the season.
- `Head to Head Stats`: Some descriptive statistics based on above table.
- `Head to Head Score Difference Probability`: Score difference probabilites based on the above table (Please account for Skew & Kurtosis). 
- `Scaled Points Stats`: Some descriptive statistics based on matches between the Historical Start & End days. Each observation used in this dataset was scaled by the relative strength of the opponent. This was done so that performance in each game can be comparable regardless of the opponent and across games. The scaling is based on custom team ranking calculations.

## Future Work

- The local Sqlite database currently does not account for data that was saved in the middle of a game. For example, if we run this at the start of a game, we might be stuck with the 0 points 0 assists e.t.c.
- Add Interactive Graphs


## License

Nba-stats-dragon CLI tool is licensed under the MIT License. See the LICENSE file for more information.

## Contributing

Contributions to nba-stats-dragon are welcome! If you find a bug or have a feature request, please open an issue on GitHub. If you would like to contribute code, please fork the repository and submit a pull request.
