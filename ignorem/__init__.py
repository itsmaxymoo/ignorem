import sys
from ignorem import commands

PROGRAM_NAME = "ignorem"
PROGRAM_NAME_FULL = "gitignore manager"
PROGRAM_VERSION = "1.0"
PROGRAM_AUTHOR = "Max Loiacono"
PROGRAM_DESCRIPTION = "Easily manage .gitignore files."
PROGRAM_URL = "https://github.com/itsmaxymoo/ignorem"
PROGRAM_CMD = "ignorem"

def _main():
	# Command line args
	num_args = len(sys.argv)
	if num_args <= 1:
		commands._command_help()
	else:
		# Make all arguments lowercase so things are easier
		for i in range(1, num_args):
			sys.argv[i] = sys.argv[i].lower()
		
		# Get the main command (first argument)
		cmd = sys.argv[1]
		# Get an array of all other arguments if they exist.
		args = [] if num_args == 2 else sys.argv[2:]

		if cmd == "add":
			commands._command_add(args)
		elif cmd == "remove":
			commands._command_remove(args)
		elif cmd == "list":
			commands._command_list()
		elif cmd == "list-all":
			commands._command_list_all()
		elif cmd == "help":
			commands._command_help()
		else:
			print("Command \"" + cmd + "\" not found.")
			print("Run \"" + PROGRAM_CMD + " help\" for usage.")
