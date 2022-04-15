import threading
from time import sleep


def do_job(number):
    sleep(3)
    print(f"Job {number} finished")


# rewrite everything inside this main function and keep others untouched
def main():
    threads = []
    for i in range(5):
        # create 5 threads
        threads.append(threading.Thread(target=do_job, args=(i,)))
        threads[i].start()
        # sleep(0.01)
main()
