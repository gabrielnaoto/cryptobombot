from controller.worker import Worker
import time

def main():
    worker = Worker()
    while True:
        try:
            worker.execute()
            time.sleep(10) # meaning that the worker will put all workers to work each 10 secs
        except Exception:
            worker.restart()

if __name__ == "__main__":
    main()
