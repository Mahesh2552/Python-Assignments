import time
import schedule

def check_email_updates():
    print("Checking email.....")

def main():
    schedule.every(10).seconds.do(check_email_updates)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
