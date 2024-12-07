from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import os

app = Flask(__name__,
            static_url_path='', 
            static_folder='static')
CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), "dataset.csv")
@app.route("/")
def index():
    # Read the CSV file
    df = pd.read_csv(CSV_FILE_PATH)

    # Create a Plotly visualization
    fig = px.bar(df, x='Date', y='Revenue', title="Sample Bar Chart")
    graph_html = fig.to_html(full_html=False)

    # Pass the visualization to the template
    return render_template("index.html", graph_html=graph_html)

if __name__ == "__main__":
    app.run(debug=True)
