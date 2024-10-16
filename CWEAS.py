import difflib
from flask import Flask, render_template, jsonify
import requests
import zipfile
import io

app = Flask(__name__)

# API URL for World Bank electricity access data
api_url = "https://api.worldbank.org/v2/en/indicator/EG.ELC.ACCS.ZS?downloadformat=csv"
# Specific file name to access in the zip file
specific_file = "Metadata_Country_API_EG.ELC.ACCS.ZS_DS2_en_csv_v2_31749.csv"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/fetch-data')
def fetch_data():
    try:
        # Step 1: Download the CSV zip file from the World Bank API
        print("Sending request to World Bank API...")
        response = requests.get(api_url)

        if response.status_code == 200:
            print("Response received successfully.")
            # Step 2: Open the response content as a zip file
            zip_file = zipfile.ZipFile(io.BytesIO(response.content))

            # Debug: Print all files in the zip
            zip_files = zip_file.namelist()
            print(f"Files in the zip: {zip_files}")

            # Step 3: Check if the exact file exists
            if specific_file in zip_files:
                print(f"Exact file '{specific_file}' found in the zip.")
                file_to_read = specific_file
            else:
                # Find the closest match to the specific file
                print(f"Exact file '{specific_file}' not found. Searching for the closest match...")
                closest_match = difflib.get_close_matches(specific_file, zip_files, n=1)
                if closest_match:
                    file_to_read = closest_match[0]
                    print(f"Closest match found: {file_to_read}")
                else:
                    print("No similar files found.")
                    return jsonify({"error": "No similar files found in the zip"}), 500

            # Step 4: Read the selected file
            with zip_file.open(file_to_read) as file:
                csv_data = file.read().decode('utf-8')
                rows = csv_data.splitlines()

            # Step 5: Convert the CSV data into a list of rows
            parsed_rows = [row.split(',') for row in rows]
            print(f"Returning {len(parsed_rows)} rows from file: {file_to_read}")
            return jsonify(parsed_rows)

        else:
            print(f"Failed to fetch data: Status code {response.status_code}")
            return jsonify({"error": f"Failed to download the data. Status code: {response.status_code}"}), 500

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
