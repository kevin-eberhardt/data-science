def example(param1=None):
    print("Hello World!")
    pass

from statsmodels.stats.outliers_influence import variance_inflation_factor
import pandas as pd
import numpy as np
import statsmodels.api as sm

#imports for pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.impute import KNNImputer
from sklearn.decomposition import PCA
from scipy import stats
import os
import pickle


def fs_colinearity(df, colinearity_threshold=0.5,correlation_threshold=0.1):
    #-------------------------------------------------Colinearity-------------------------------------------------
    dropped_features = []
    # Calculate the correlation between columns
    corr_matrix = df.corr().abs()
    # Create a mask to select the upper triangle of the correlation matrix
    mask = np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)

    # Apply the mask to get the upper triangle of the correlation matrix
    upper_triangle = corr_matrix.where(mask)
    
    # Find the columns with colinearity greater than correlation_threshold
    colinear_columns = upper_triangle[upper_triangle > colinearity_threshold].stack().index
     # Get the values of colinearity
    colinearity_values = upper_triangle[upper_triangle > colinearity_threshold].stack()

    # loop through the colinear_columns and select the one with lower correlation to quality and avoid duplicates in the list
    for col1, col2 in colinear_columns:
        corr_col1 = df[col1].corr(df['label__quality'])
        corr_col2 = df[col2].corr(df['label__quality'])
        if abs(corr_col1) < abs(corr_col2):
                corr_col = df[col1].corr(df['label__quality'])
                if abs(corr_col) < correlation_threshold:
                    dropped_features.append(col1)
        else:
                corr_col = df[col2].corr(df['label__quality'])
                if abs(corr_col) < correlation_threshold:
                    dropped_features.append(col2)
              
                     
    return dropped_features

def fs_vif(df, correlation_threshold=0.1, vif_threshold=5):

    dropped_features = []

    columns_to_exclude = ['label__quality']
    # Select the columns excluding the quality label
    columns = [col for col in df.select_dtypes(exclude='object').columns if col not in columns_to_exclude]

    # Create a new dataframe with only the selected columns
    df_selected = df[columns]

    # Add a constant column to the dataframe (required for VIF calculation)
    df_selected = sm.add_constant(df_selected)

    vifToRemove = 0
    while True:
        # Calculate VIF values for remaining features
        vif = pd.DataFrame()
        vif["Variable"] = df_selected.columns
        vif["VIF"] = [variance_inflation_factor(df_selected.values, i) if np.var(df_selected.iloc[:, i]) != 0 else 0 for i in range(df_selected.shape[1])]

        # Exclude the constant column from the results
        vif = vif[1:]
        # Order the VIF values in ascending order
        vif.sort_values('VIF', ascending=False, inplace=True)
        # Check if all VIF values are below the threshold
        if all(vif.iloc[vifToRemove:, vif.columns.get_loc("VIF")] < vif_threshold):
            break

        # Find the feature with the highest VIF value
        if vifToRemove < vif.shape[0] and vif.iloc[vifToRemove]["Variable"] is not None:
            highest_vif_feature = vif.iloc[vifToRemove]["Variable"]
        
        # Check correlation of the highest VIF feature with quality label
        correlation = df[highest_vif_feature].corr(df["label__quality"])
       

        if abs(correlation) < correlation_threshold:
            # Remove the feature if correlation is below the threshold
            dropped_features.append(highest_vif_feature)
            df_selected = df_selected.drop(highest_vif_feature, axis=1)  # Drop from df_selected as well
        else:
            # Move on to the next highest VIF feature
            vifToRemove = vifToRemove + 1
    
   
    return dropped_features

def outlier_label(df):
    """This function detects outliers in the dataframe and imputes them with KNNImputer.
    :param df: dataframe with only the label
    """
    #detect outliers and impute them with the simple imputer

    #delete all rows where the label is > 10
    df = df[df.iloc[:, df.shape[1]-1] <= 10]

    # z = np.abs(stats.zscore(df.iloc[:, df.shape[1]-1]))
    # df.iloc[:, df.shape[1]-1][(z >= 3)] = np.nan

    #impute last column with KNNImputer
    # imputer = KNNImputer(n_neighbors=5).set_output(transform="pandas")
    # df.iloc[:, df.shape[1]-1] = imputer.fit_transform(df)


    #make all label values integers
    #df.iloc[:, df.shape[1]-1] = df.iloc[:, df.shape[1]-1].astype(int)
    #cast to float
    #df.iloc[:, df.shape[1]-1] = df.iloc[:, df.shape[1]-1].astype(float)
    
    return df

def outlier_num(df, strategy='median'):
    """This function detects outliers in the dataframe and imputes them with the median.
    :param df: dataframe with only numerical features
    :param strategy: choose median, mean  most_frequent method. Defaul = median
    """
    #detect outliers and impute them with the simple imputer
    #detect outliers
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1

    #detect outliers for each column and set them to NaN
    for col in df.columns:
        df.loc[(df[col] < (Q1[col] - 1.5 * IQR[col])) | (df[col] > (Q3[col] + 1.5 * IQR[col])), col] = np.nan

    #impute outliers with median
    if strategy == 'median':
        imputer = SimpleImputer(strategy='median').set_output(transform="pandas")
        df = imputer.fit_transform(df)
    #impute outliers with mean
    elif strategy == 'mean':
        imputer = SimpleImputer(strategy='mean').set_output(transform="pandas")
        df = imputer.fit_transform(df)
    #impute outliers with most frequent value
    elif strategy == 'most_frequent':
        imputer = SimpleImputer(strategy='most_frequent').set_output(transform="pandas")
        df = imputer.fit_transform(df)
    else:
        #impute outliers with median
        imputer = SimpleImputer(strategy='median').set_output(transform="pandas")
        df = imputer.fit_transform(df)

    return df



def dim_reduction(df, n_components=0.95):
    """This function applies dimensionality reduction to the dataframe.
    :param df: dataframe with only numerical features
    :param n_components: threshold for the explained variance (default=0.95)
    """
    #dimensionality reduction with PCA
    #we want the explained variance to be 95%. 
    #with choosing n_components=0.95,
    #PCA will return the minimum number of principal components 
    #at which 95% of the variance is retained.
    pca = PCA(n_components)
    #apply pca to numerical features
    df = pca.fit_transform(df)

    #write pca to a pickle file
    import pickle
    with open('\models\pca.pickle', 'wb') as outfile:
        pickle.dump(pca, outfile)

    return df

#load models from ./task_2/models
def load_best_models():
    models = []
    dirname = "./models"
    for file in os.listdir(dirname):
        if file.endswith('.pkl'):
            # load pickle file
            dir = os.path.join(dirname, file)  # Construct the full path
            model = pickle.load(open(dir, 'rb'))
            models.append(model)  # Append the loaded model to the list
    return models

