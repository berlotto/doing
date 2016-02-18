# -*- encoding: utf-8 -*-
# Doing 
# A simple timetracker
#
# Author: Sérgio Berlotto Jr <sergio.berlotto@gmail.com>
#

import dataset
import os
from core import main, command
from datetime import datetime
from colorama import Fore, Back, Style

def console_size():
	rows, cols = os.popen("stty size","r").read().split()
	return int(rows), int(cols)

def message(text):
	print(Style.BRIGHT + Fore.YELLOW + " -> " + Fore.GREEN + text + Fore.RESET)

def separator():
	print(Fore.BLUE + Style.BRIGHT + "-"*console_size()[1] + Style.RESET_ALL)

db = dataset.connect('sqlite:///doing.db')
table_tasks = db['tasks']

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = #
# COMMANDS CONTROL
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = #

@command("start", help="Start new task, restart if paused, stop latest task if started")
def start(name, *tags):
	
	current_task = table_tasks.find_one(current=True)
	if current_task:
		current_task['stop'] = datetime.now()
		current_task['current'] = False
		table_tasks.update(current_task, ['id'])
		print("Task '%s' stoped!" % current_task['name'])

	if tags:
		task_tags = tags
	else:
		task_tags = []
	str_task_tags = ",".join(task_tags)
	table_tasks.insert(dict(name=name,tags=str_task_tags,notes="",start=datetime.now(),stop=None,current=True))
	message("New task '%s' added!" % name)

@command("tag",help="Tag last/current entrie")
def tag(*tags):
	current_task = table_tasks.find_one(current=True)
	task_tags = current_task['tags']
	
	if task_tags:
		task_tags = task_tags.split(",")
	
	for tag in tags:
		task_tags.append(tag)
	
	current_task['tags'] = ",".join(task_tags)
	table_tasks.update(current_task, ['id'])

	message("Tag(s) '%s' added in current task !" % ",".join(tags) )

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