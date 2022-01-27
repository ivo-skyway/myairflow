import json
from datetime import datetime
from time import sleep

now = datetime.now()
start = now
version = "0.1.27.3"


def print_hello():
    tries = 10

    with open("/tmp/mylog", "wt") as f:
        for i in range(tries):
            msg = f'loop {i + 1}/{tries}  Hello world v.{version} time now: {datetime.now()}'
            f.write(msg + "\n")
            f.flush()
            print(msg)
            sleep(10)

    xcom_return = {"key1": tries, "key2": "OK"}
    # xcom push
    with open("/airflow/xcom/return.json", "w") as file:
        json.dump(xcom_return, file)

    return "OK"


if __name__ == "__main__":
    print_hello()
