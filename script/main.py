import csv
import time
from loguru import logger
from db import write_to_database


logger.add("main.log", format="{time} {level} {message}", level="DEBUG",
           rotation="100 Mb", compression="zip")


@logger.catch
def read_and_write_data(file: str) -> None:
    """read data from csv file and write to database"""

    logger.debug(f"Start")
    count = 0
    start = time.monotonic()
    with open(file) as _file:
        csv_file = csv.reader(_file)
        for line in csv_file:
            if count == 0:
                count += 1 # pass first row
            else:
                count += 1
                write_to_database(line)
    logger.debug(f"records made {count-1}")
    logger.debug(f"execution time {time.monotonic() - start}")
        

if __name__ == "__main__":
    read_and_write_data("f.csv")
