import time

from worker import Worker
from control import Control

def main():
    worker = Worker()
    while True:
        try:
            worker.execute()
            time.sleep(10)
        except Exception:
            worker.restart()

if __name__ == "__main__":
    main()
