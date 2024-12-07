from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px
import os
from get_csv_headers import get_csv_headers  # Import the get_csv_headers function from another file

app = Flask(__name__, static_url_path='', static_folder='static')
app.config['UPLOAD_FOLDER'] = 'uploads'  # Define the folder for uploaded files
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    graph_html = None
    error_message = None
    headers = []

    if request.method == "POST":
        # Check if a file is uploaded
        file = request.files.get('csv_file')
        if file and file.filename.endswith('.csv'):
            # Save the uploaded file
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Get column headers using the imported function
            headers = get_csv_headers(file_path)

            # Process the file and create the visualization
            try:
                df = pd.read_csv(file_path)

                # Check for required columns based on dynamic headers
                if all(header in df.columns for header in headers):
                    fig = px.bar(df, x=headers[0], y=headers[1], title="Revenue Over Time")
                    graph_html = fig.to_html(full_html=False)
                else:
                    error_message = f"CSV file must contain {', '.join(headers)} columns."
            except Exception as e:
                error_message = f"Error reading the file: {str(e)}"
        else:
            error_message = "Invalid file type. Please upload a valid CSV file."

    return render_template("index.html", graph_html=graph_html, error_message=error_message, headers=headers)

if __name__ == "__main__":
    app.run(debug=True)
