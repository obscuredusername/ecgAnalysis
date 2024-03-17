import pandas as pd
import matplotlib.pyplot as plt

def plot_ecg_measurements():
    # Read the CSV file into a DataFrame
    df = pd.read_csv('./result_folder/required.csv')

    # Get the time column
    time = df['time']

    # Get the column names for all leads
    lead_columns = df.columns[df.columns != 'time']

    # Create the plot
    plt.figure(figsize=(10, 6))
    for lead_column in lead_columns:
        plt.plot(time, df[lead_column], label=lead_column)

    # Customize the plot
    plt.xlabel('Time')
    plt.ylabel('Voltage (mV)')
    plt.title('ECG Measurements')
    plt.legend()

    # Display or save the plot
    plt.show()

# Call the function
plot_ecg_measurements()
