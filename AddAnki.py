import subprocess


def addAnki(front, back, deck):
	card = "[\"" + front + "\",\"" + back + "\"]"
	# TODO ankictlのプルリクが通ったらこっちを有効にする
	#cmd = ["ankictl", "-A", deck, "-i", card]
	cmd = ["./ankictl", "-A", deck, "-i", card]
	p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	return p.communicate()[0]