import subprocess
import os


def addAnki(front, back, deck):
	card = "[\"" + front + "\",\"" + back + "\"]"
	cmd = [os.environ["HOME"]+"/.go/bin/ankictl", "-A", deck, "-i", card]
	p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	return p.communicate()[0]