#!/usr/bin/python

import time

class PythonTimer:
  # This is a python class.

  # Constructor
  def __init__ (self, arg1, arg2)
    timeLeft = 15
    paused = false
    started = false
  
  # Returns the amount of time left on the timer
  def getTime(self):
    return timeLeft

  # Starts the timer, decreasing the time every second
  def run(self):
    started = true
    while count > 0:
      if !paused:
        timeLeft--
        sleep(1)
        print timeLeft

  # Pauses the timer
  def pause(self):
    paused = true

  # Unpauses the timer
  def unpause(self):
    if started: 
      paused = false
