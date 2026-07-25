from datetime import datetime

with open("daily_etl.log", "a") as f:
    f.write(f"ETL executed at {datetime.now()}\n")

