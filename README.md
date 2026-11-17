# Weather ETL Pipeline

Ứng dụng ETL đơn giản để lấy dữ liệu dự báo thời tiết tại Hà Nội từ Open-Meteo API, xử lý dữ liệu và lưu vào SQLite.

## Project Structure

```text
Weather Analyst/
|-- data/
|   `-- weather.db           # SQLite database created when the pipeline runs
|-- sql/
|   |-- init.sql             # Create bronze_weather table
|   |-- insert_data.sql      # Insert weather records
|   |-- read_all.sql         # Read all stored records
|   `-- truncate.sql         # Clear old records before loading new data
|-- create_database.py       # Create the SQLite database and table
|-- extract.py               # Fetch forecast data from Open-Meteo API
|-- transform.py             # Clean and format the weather data with pandas
|-- load.py                  # Load today's data into SQLite
|-- query.py                 # Display all data in bronze_weather
|-- main.py                  # Run the ETL pipeline
|-- show.py                  # Show and plot temperature for a selected day
|-- requirements.txt         # Python dependencies
`-- README.md
```

## Stack

- **Python**
- **Open-Meteo API**: weather forecast data source
- **pandas**: data transformation
- **SQLite**: local database
- **Matplotlib**: temperature chart
- **requests**: API request

## Data Flow

```text
Open-Meteo API -> extract.py -> transform.py -> load.py -> SQLite (data/weather.db)
```

The current default location is Hanoi. The API response contains hourly temperature data; the pipeline keeps the selected date, hour, temperature, and a generated ID.

## Installation

### 1. Clone project

```bash
git clone https://github.com/DinhNguyenNgocMinh/WeatherApp.git
cd WeatherApp
```

### 2. Create and activate virtual environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Usage

### Run ETL pipeline

```bash
python main.py
```

The program will:

1. Create `data/weather.db` and the `bronze_weather` table if they do not exist.
2. Get the current day's hourly forecast for Hanoi.
3. Clear old records and insert the new data into SQLite.
4. Wait for Enter, then print all records in `bronze_weather`.

### Show temperature chart

```bash
python show.py
```

Enter a date from today to six days later. Leave day or month blank to use today's value. The program prints the selected data and opens its temperature chart.

## Notes

- Python 3.8 or newer is recommended.
- `datetime` and `sqlite3` are built into Python; no separate installation is required for them.
- Each run of `main.py` removes the existing records in `bronze_weather` before loading the latest result.
