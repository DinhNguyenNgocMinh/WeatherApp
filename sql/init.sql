CREATE TABLE IF NOT EXISTS bronze_weather (
    id TEXT NOT NULL,
    temperature TEXT NOT NULL,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    uploaded_at DEFAULT CURRENT_TIMESTAMP
)