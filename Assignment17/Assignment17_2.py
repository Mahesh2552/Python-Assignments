import time
import datetime
import schedule

def display_current_datetime():
    print(datetime.datetime.now())

def main():
    schedule.every(1).minute.do(display_current_datetime)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()