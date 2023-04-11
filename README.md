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


### Tasks
#### Task 1a: Infrastructure
Conceptualize your analysis architecture including 
(elements, technology and environment)
– Data provisioning (data model and staging)
– Data consumption (structure of your analysis scripts)

Implement this architecture
– Data provisioning
– Stubs for data consumption

#### Task 1b: Exploration
Explore the (provided) data set using descriptive statistics (e.g. mean values, standard deviations, min/max values, missing values) and visualizations (e.g. histograms, boxplots) Point out which data quality issues you identified in terms of
– Missing values
– Noise
– Outliers
– Features to be transformed, standardized or normalized 
Point out which data reduction actions would make sense from your perspective in terms of 
– Feature selection
– Instance selection

#### Task 2: Preprocessing and Modeling
Create a baseline model using the originally provided dataset with minimal preprocessing and evaluate it based on accuracies, using the training & validation subset of the data Optimize your model by the following measures
– Data Preprocessing: Preprocess the original dataset to address the identified issues applying different strategies for each issue
    - data quality issues (Missing values, Noise, Outliers, Transformations)
    - data reduction issues (Feature and Instance Selection)
– Algorithm Selection: Experiment with different regression algorithms, e.g. linear regression, polynomial regression, regression trees etc.
– Hyper-parameter Tuning: Change the hyper-parameters of your algorithms (e.g. „degree“ in case of polynomial regression)

Implement a grid search to run and evaluate your different model options
Your grid search should
– Receive a configuration JSON file as an input, including:
    - Preprocessing steps to be conducted
    - (Hyper-) Parameters of the preprocessing methods / algorithms
    - Modeling algorithm to be applied
    - Hyper-Parameters of the modeling algorithm
– Train and Validate models in an automated fashion, based on the grid search configuration file
– Log all evaluation results (Validation and Test accuracies)
– Display an overview of all evaluation results in the end

Additionally to the training and validation examples provided, there will be test examples, which you will receive at the day of the presentation to challenge your models
Prepare to be ready to apply these test examples to your best model – they will have a similar structure like the training examples

https://e-learning.hdm-stuttgart.de/moodle/pluginfile.php/452840/mod_resource/content/2/2023_DS3_Intro_and_CaseDescription.pdf
