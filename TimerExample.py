import time
from threading import Thread

class Timer:
    def __init__(self, timeSec: int):
        self.__sec = timeSec
        self.__timeThread = None
        self.__ready = True
        self.__stoped = False

    def check(self):
        return self.__ready

    def start(self):
        self.__timeThread = Thread(target=self. __internal_start)
        self.__timeThread.start()

    def __internal_start(self):
        self.startTime = time.time()
        self.__ready = False
        print("start jump")
        while True and not self.__stoped:
            print("Is jumping.")
            currentTime = time.time()
            elapsedTime = currentTime - self.startTime
            if elapsedTime > self.__sec:
                break

            time.sleep(0.1)

        print("Jump finished.")
        self.__ready = True

    def stop(self):
        self.__stoped = True