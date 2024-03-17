import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import os

def perform_pca_and_visualization():
    # Load ECG data from the CSV file
    data = pd.read_csv('./result_folder/required.csv')

    # Extract ECG signal data (excluding the 'time' column)
    X = data.iloc[:, 1:].values

    # Apply PCA
    pca = PCA(n_components=6)  # Reduce to 6 principal components
    X_pca = pca.fit_transform(X)

    # Create a new DataFrame with the principal components and time
    df_pca = pd.DataFrame({'time': data['time']})
    for i in range(6):
        df_pca[f'PC{i+1}'] = X_pca[:, i]

    # Plot the first 6 principal components against time
    plt.figure(figsize=(12, 6))
    for i in range(6):
        plt.plot(df_pca['time'], df_pca[f'PC{i+1}'], label=f'Principal Component {i+1}')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('ECG Signals Projected onto the First Six Principal Components')
    plt.legend()
    plt.savefig('./result_folder/PC6_plot.png')  # Save plot as PNG
    plt.show()

    # Compute correlation matrix of the principal components
    corr_matrix_pca = df_pca.corr()

    # Plot correlation matrix of the principal components as a heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix_pca, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix of the First Six Principal Components')
    plt.savefig('./result_folder/PC6_heatmap.png')  # Save heatmap as PNG
    plt.show()

    # Save PCA-reduced data
    df_pca.to_csv('./result_folder/pca_reduced_data.csv', index=False)

# Call the function
perform_pca_and_visualization()
