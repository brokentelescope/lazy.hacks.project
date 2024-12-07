from kaggle.api import KaggleApi

api = KaggleApi()
api.authenticate()














@app.route('/search', methods=['POST'])
def search_datasets():
    keyword = request.form['keyword']
    try:
        # Search for datasets
        datasets = api.dataset_list(search=keyword, page_size=10)
        results = [{"title": d.title, "ref": d.ref} for d in datasets]
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    

@app.route('/download', methods=['POST'])
def download_dataset():
    dataset_ref = request.form['dataset_ref']  # Example: 'zillow/zecon'
    try:
        # Download the dataset
        api.dataset_download_files(dataset_ref, path=DOWNLOAD_FOLDER, unzip=True)
        return jsonify({"message": f"Dataset '{dataset_ref}' downloaded successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
