import time

from worker import Worker
from control import NeedsRestartException

def main():
    time.sleep(5)
    worker = Worker()
    while True:
        try:
            worker.execute()
            time.sleep(2)
        except NeedsRestartException:
            worker.restart()

if __name__ == "__main__":
    main()
