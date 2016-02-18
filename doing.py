#!/usr/bin/python
# -*- encoding: utf-8 -*-
# Doing 
# A simple timetracker
#
# Author: Sérgio Berlotto Jr <sergio.berlotto@gmail.com>
#

from core import main, command

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = #
# COMMANDS CONTROL
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = #

@command("start", help="Start new task, restart if paused, stop latest task if started")
def start(name, *tags):
	print("Command START")
	print(name, tags)

@command("tag",help="Tag last/current entrie")
def tag(*tags):
	print("Command TAG")
	print(tags)

@command("note",help="Add note to last/current task")
def note(text):
	print("Command Note: %s" % text)

@command("pause",help="Add a pause for a task X time (Xm, Xh)")
def pause(time):
	print("Command Pause: %s" % time)

@command("finish",help="Finish the current task")
def finish():
	print("Command finish ")

@command("show",help="Show current task information")
def show():
	print("Command show ")

@command("list",help="List all tasks")
def list():
	print("Command List ")

@command("recent",help="List last recent tasks")
def recent():
	print("Command recent ")

@command("today",help="List all today tasks")
def today():
	print("Command today ")

@command("yestarday",help="List all yesterday tasks")
def yestarday():
	print("Command yestarday ")

@command("grep",help="List tasks matching text, tag or pattern")
def grep(pattern):
	print("Command grep ")


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = #
# MAIN CALL
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = #

if __name__ == '__main__':
	main()