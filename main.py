import shutil
from flask import Flask, render_template, request
import os
from csvfile import process_file
from denoise import denoise_csv
from PCA import perform_pca_and_visualization
from visualization import plot_ecg_measurements

app = Flask(__name__)

# Define the upload directory
UPLOAD_FOLDER = './upload/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Define the result folder for processed CSV files
RESULT_FOLDER = './result_folder/'
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    # Get the list of files in the upload folder
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)


@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        # Get the uploaded files
        file1 = request.files['file1']
        file2 = request.files['file2']

        # Check if both files are provided
        if file1.filename == '' or file2.filename == '':
            return 'Please select two files'

        # Save the uploaded files to the upload directory
        file1_path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file2_path = os.path.join(app.config['UPLOAD_FOLDER'], file2.filename)
        file1.save(file1_path)
        file2.save(file2_path)

        # Remove file extension from file1
        file1_name_without_extension, file1_extension = os.path.splitext(file1.filename)
        x= UPLOAD_FOLDER + file1_name_without_extension

        # Process the uploaded files
        process_file(x, RESULT_FOLDER)
        plot_ecg_measurements()
        shutil.rmtree(UPLOAD_FOLDER)
        denoise_csv()

        plot_ecg_measurements()
        perform_pca_and_visualization()
       
        # Get the paths of the generated PNG files
        pc6_plot_path =  'PC6_plot.png'
        pc6_heatmap_path =  'PC6_heatmap.png'
        
        return render_template('thankyou.html', pc6_plot=pc6_plot_path, pc6_heatmap=pc6_heatmap_path)
    except Exception as e:
        return f'Error processing files: {str(e)}'


if __name__ == '__main__':
    app.run(port=8080)
