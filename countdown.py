# import the time module
import time

# define the countdown func.
def countdown(time_in_sec):

    while time_in_sec:
        mins, secs = divmod(time_in_sec, 60)                #divmod() method takes two number and returns a pair of 
                                                             #number(a tuple) consisting of their quoitent and remainder.
        timertime = '{:02d}:{:02d}'.format(mins, secs)
        print(timertime, end="\r")
        time.sleep(1)
        time_in_sec -= 1

        print('Tik Tok Tik!!')


# input the time in seconds
t = input("Enter the time in seconds: ")

# function call
countdown(int(t))