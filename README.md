The World Electricity Access Sorter is a Python-based project designed to acquire, process, and analyze global electricity access data from CSV files. The project automates the downloading, unzipping, and sorting of data, with a focus on providing insightful analyses regarding the percentage of a population with access to electricity. The system identifies and processes country-specific data, even when the exact file is unavailable, selecting the closest match to ensure continuous functionality.

Key Features:
Automated Data Acquisition:

Downloads and extracts data from a zip archive, accessing global electricity access statistics in CSV format.
Target file: Metadata_Country_API_EG.ELC.ACCS.ZS_DS2_en_csv_v2_31749. If this file is unavailable, the system intelligently selects the closest available file from the dataset, ensuring that data processing can continue uninterrupted.
Data Processing & Analysis:

Reads, cleans, and validates electricity access data from the CSV file using Python’s built-in libraries.
Analyzes electricity access statistics for various countries, focusing on key metrics like the percentage of population with access to electricity.
Sorts countries by electricity access levels, providing insights into global disparities and trends in energy availability.
Error Handling:

Includes robust error handling to manage file mismatches, missing data, and formatting inconsistencies.
If the exact target file isn't found, the program searches for the most similar file name within the directory, providing seamless fallback functionality.
Data Output:

Outputs the results of the analysis in a well-structured HTML format, allowing users to view country-level electricity access data.
Interactive and responsive design for displaying sorted lists of countries, highlighting regions with the highest and lowest electricity access.
Customizable & Extendable:

Easily configurable to work with different datasets or metrics related to electricity access or energy availability.
Future extensions could include visualizations, interactive charts, or additional metrics for deeper insights into energy access worldwide.
How It Works:
File Acquisition: The project downloads a zip file containing CSV data from a predefined URL.
File Handling: It automatically selects the exact CSV file or the closest match to the target file, Metadata_Country_API_EG.ELC.ACCS.ZS_DS2_en_csv_v2_31749.
Data Parsing: Reads and parses the CSV file, handling various edge cases, including missing or malformed data.
Sorting & Analysis: Sorts countries by electricity access percentages and performs basic statistical analysis on the dataset.
HTML Output: Displays the sorted results on an HTML page, which can be viewed in a web browser for easy sharing and interpretation.
