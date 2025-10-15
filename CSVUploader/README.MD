# Project: CSV Uploader 🚀

A simple and efficient Python tool to upload CSV data. This project was inspired by the need for a handy and reusable CSV uploading utility in a professional development environment.

## Overview

This script provides a straightforward way to take a CSV file
---

## Features ✨

* **Efficient Processing**: Reads and processes large CSV files without consuming excessive memory.
* **Easy Configuration**: Simple setup for database connections and other settings.
* **Error Handling**: [e.g., Skips bad rows and logs errors for later review.]
* **Validation**: [e.g., Ensures that the CSV has the required columns before processing.]

## Requirements

Before you begin, ensure you have the following installed:
* Python 3.x
* PIP (Python package installer)

This project relies on the following Python packages:
* `[ pandas]`

* `[ psycopg2-binary for PostgreSQL]`
* `[ python-dotenv for environment variables]`

---

## Usage ⚙️

1.  **Run the script:**
    Execute the main script from your terminal, providing the path to your CSV file and the target table name.
    ```bash
    python uploader.py --file /path/to/your/data.csv --table_name my_target_table
    ```
    
    **Arguments:**
    * `--file`: The full path to the CSV file you want to upload.
    * `--table_name`: The name of the database table where the data should be inserted.

---

## How It Works

The script performs the following steps:
    [step 1 hasn't been compeleted yet... stay tuned for that oen :P]
1.  Connects to the database using the credentials from the `.env` file.
2.  Reads the CSV file and currently goes through the top row and displays the data you require
3.  Iterates through each row and inserts it into the specified database table.
4.  Logs any errors encountered during the process to `[e.g., uploader.log]`.

---

## Contributing 🤝

Contributions are welcome! If you have suggestions for improvements, please feel free to create an issue or submit a pull request.

1.  Fork the Project.
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the Branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

---

## License

This project is licensed under Tshepang Mlambo