#!/usr/bin/python
# -*- encoding: utf-8 -*-
# Doing 
# A simple timetracker
#
# Author: Sérgio Berlotto Jr <sergio.berlotto@gmail.com>
#

import sys

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = #
# MAIN CONTROL
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = #

commands = {}
helps = {}

def command(name, help=None):
	# Guarda os comandos e suas respectvas funções para chamar conforma
	# parametros recevidos no script
	def decorate(func):
		if help:
			helps[name] = help
		commands[name] = func
		# print(func,name)
	return decorate


def usage():
	print("doing - A nerd time-tracker for terminal")
	print(" ")
	print("COMMANDS:")
	print(" ")
	for command in commands.keys():
		if command in helps.keys():
			print(" %s\t\t%s" % (command,helps[command]))
		else:
			print(" %s" % command)
	print(" -h|--help\tThis help text")
	print("\n\nTks for using doing")
	print("https://github.com/berlotto/doing")



def main():
	args = sys.argv[1:]

	if not args or args[0] == "-h" or args[0] == "--help":
		usage()
	else:
		if not args[0] in commands.keys():
			print ("'%s' is not a valid command. Use --help or -h" % args[0])
		else:
			#Treat the strings parameters
			arguments = []
			strparam = []
			for arg in args[1:]:
				if arg.startswith("@") or arg.startswith("-"):
					if strparam:
						arguments.append(" ".join(strparam))
						strparam = []
					arguments.append(arg)
				elif "=" in arg:
					if strparam:
						arguments.append(" ".join(strparam))
						strparam = []
					arguments.append(arg.split("="))
				else:
					strparam.append(arg)

			if strparam:
				arguments.append(" ".join(strparam))
				strparam = []

			try:
				commands[args[0]](*arguments)
			except TypeError as e:
				if "missing" in str(e):
					print("Some parameters for '%s' command are missing" % args[0])
				else:
					commands[args[0]]()
