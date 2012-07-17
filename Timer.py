#!/usr/bin/python

import time

class PythonTimer:
  # This is a python class.

  # Constructor
  def __init__ (self, time):
    self._time_left = time
    self.paused = False
    self.running = False
  
  # Returns the amount of time left on the timer
  def get_time_left(self):
    return self._time_left

  def set_time_left(self, time):
    self._time_left = time

  time_left = property(get_time_left, set_time_left)

  # Starts the timer, decreasing the time every second
  def start(self):
    self.running = True
    while self.time_left > 0:
      if not self.paused:
        self.time_left -= 1
        time.sleep(1)
        print self.time_left
    self.running = false

  # Pauses the timer
  def pause(self):
    self.paused = True

  # Unpauses the timer
  def unpause(self):
    if self.running: 
      self.paused = False
