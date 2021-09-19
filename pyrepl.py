import tty, termios
import sys

mode = "PYREPL"

while True:
	print("{} > ".format(mode), end='')
	sys.stdout.flush()
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(fd)
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	print("")
	print("Ch was {}".format(ch))
	if (ch == "]"):
		mode = "Install"
	elif (ch == "/"):
		mode = "PYREPL"
	elif (ch == "q"):
		break
