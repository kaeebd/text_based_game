name = None

def output(text):
	print text

def getInput(text=""):
	return raw_input(text)

def main():
	global name
	name = raw_input()

def askQuestion(question, options):
	output(question)
	for i in range(len(options)):
		output(str(i+1) + "- " + options[i])
	while True:
		inp = getInput("> ")
		if not inp.isdigit():
			continue
		inp = int(inp)
		if inp >= 1 and inp <= len(options):
			return inp

#Testing:

def intro():
	ans = askQuestion("\"How are you?\"", ["\"Good.\"", "\"Bad.\"", "\"Terrific.\"", "\"Horrible.\""])
	if ans == 1:
		output("\"Awwwww that's good.\"")
	elif ans == 2:
		output("\"Awwwww that sucks.\"")
	elif ans == 3:
		output("\"Awwwww that's great.\"")
	elif ans == 4:
		output("\"Awwwww that's terrible.\"")
intro()
