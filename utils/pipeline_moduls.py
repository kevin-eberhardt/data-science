def example(param1=None):
    print("Hello World!")
    pass

from statsmodels.stats.outliers_influence import variance_inflation_factor
import pandas as pd
import numpy as np
import statsmodels.api as sm


def fs_colinearity(df, colinearity_threshold=0.5,correlation_threshold=0.1):
    #-------------------------------------------------Colinearity-------------------------------------------------
    dropped_features = []
    print(9*"\n")
    print("--------Colinearity--------"+ "\n")
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
        print("High Colinearity between " + col1 + " and "+col2 + " with a value of " + str(colinearity_values[col1, col2]))
        if abs(corr_col1) < abs(corr_col2):
                corr_col = df[col1].corr(df['label__quality'])
                if abs(corr_col) < correlation_threshold:
                    print("Dropping " + col1 + " because of low correlation "+str(corr_col1)+" with quality"+ "\n")
                    df = df.drop(col1, axis=1)
                    dropped_features.append(col1)
                else:
                    print("Not Dropping " + col1 + " because of high correlation "+str(corr_col1)+" with quality"+ "\n")

        else:
                corr_col = df[col2].corr(df['label__quality'])
                if abs(corr_col) < correlation_threshold:
                    print("Dropping " + col2 + " because of low correlation "+str(corr_col)+" with quality"+ "\n")
                    df = df.drop(col2, axis=1)
                    dropped_features.append(col2)
                else: 
                    print("Not Dropping " + col2 + " because of high correlation "+str(corr_col)+" with quality"+ "\n")
                     
    print("HI")

    print("Every colinearity is below the threshold of "+str(colinearity_threshold)+"! \n")
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

    print("--------VIF--------"+ "\n")
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
            print("Every VIF is below the threshold of "+str(vif_threshold)+"! \n")
            break

        # Find the feature with the highest VIF value
        if vifToRemove < vif.shape[0] and vif.iloc[vifToRemove]["Variable"] is not None:
            highest_vif_feature = vif.iloc[vifToRemove]["Variable"]
        
        # Check correlation of the highest VIF feature with quality label
        correlation = df[highest_vif_feature].corr(df["label__quality"])
        print("Highest VIF Value, Feature: " + str(highest_vif_feature) + " with a value of " + str(vif.iloc[vifToRemove]["VIF"]))
       

        if abs(correlation) < correlation_threshold:
            # Remove the feature if correlation is below the threshold
            print("Dropping " + highest_vif_feature + " because of low correlation "+str(correlation)+" with quality"+ "\n")
            dropped_features.append(highest_vif_feature)
            df = df.drop(highest_vif_feature, axis=1)
            df_selected = df_selected.drop(highest_vif_feature, axis=1)  # Drop from df_selected as well
        else:
            print("Not Dropping " + highest_vif_feature + " because of high correlation "+str(correlation)+" with quality"+ "\n")
            # Move on to the next highest VIF feature
            vifToRemove = vifToRemove + 1
    
   
    return dropped_features