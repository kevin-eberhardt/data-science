# Data Science

## Getting Started

### Prerequisites

- [Python 3.11](https://docs.python.org/release/3.11.3/whatsnew/3.11.html)

### Installing

First install the requirements by running following command in the directory:

```python
pip install -r requirements.txt
```

or

```python
conda create --name <envname> --file requirements.txt
```

After that, you have to setup the environment variables:

1. Copy `.env.example` to `.env`
2. Fill in the variables
3. Run notebooks/data_exploration.ipynb to check if dataset is loaded correctly

## Environment Variables

| Variable            | Description                                |
| ------------------- | ------------------------------------------ |
| `DB_HOST`           | Path to the MySQL database                 |
| `DB_USER`           | MySQL User                                 |
| `DB_PASSWORD`       | MySQL Password                             |
| `DB_NAME`           | MySQL Database Name                        |
| `DB_PORT`           | MySQL Port                                 |
| `WORKING_DIRECTORY` | Path of the directory python is running in |

_WORKING_DIRECTORY_: You can get the path of your working directory by typing `pwd` in your directory in the terminal where the README is stored
