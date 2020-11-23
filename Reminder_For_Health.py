from pygame import mixer
from datetime import datetime
from time import time


def musicOnLoop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break


def log_now(msg):
    with open("myLog.txt", "a") as fp:
        fp.write(f"{msg}  {datetime.now()}\n")


if __name__ == "__main__":
    _initWater = time()
    _initEyes = time()
    _initExercise = time()
    while True:
        if(time()-_initWater > 5):
            print("Enter Drank to stop the music")
            musicOnLoop("water.mp3", "drank")
            _initWater = time()
            log_now("Drank water at ")

        if(time()-_initEyes > 10):
            print("Enter 'done' to stop the music for eye exercise")
            musicOnLoop("eyes.mp3", "done")
            _initEyes = time()
            log_now("Eye Exercise done at ")

        if(time()-_initExercise > 15):
            print("Enter 'done' to stop the music for physical exercise")
            musicOnLoop("Exercise.mp3", "done")
            _initExercise = time()
            log_now("Pysical Exercise Done exercise at ")
