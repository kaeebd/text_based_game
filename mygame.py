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
			
def intro():
	global name
	output("\n\"Ah... And so enters a new adventurer. Please, allow me to give you a warm and proper welcome.\"\n")
	
	output("The anomalous velvety voice of a young woman gently interrupts the dead silence as the sharp flick "
		"of a match echoes through the voidish blackness of the cavernous room, and a soft golden orb of firelight "
		"manifests around a pale feminine face.")
	
	output("\n\"And do relish it, will you?"
		" Most all of the ones that came before you so hastily took for granted the kindness I tried to give."
		" Not to say I believe you are like them.\"")

	output("\nSuddenly, I couldn't seem to feel the presence of my body, for "
		"an overwhelming numbness took over me as the room seemed to "
		"sing an uncomfortable yet familiar coldness.")

	output("\n\"No... On the contrary, in fact. I can tell you're a different sort.\n" 
		"Either way, just don't be too terribly offended if the people and the land do not take a liking to you.\"\n")

	output("As if my voice had been stolen from me, I could not choke out a single sound, let alone a word. "
		"I was frozen in time and space, mesmerized in the most debiliating way. The gravity seemed ten times "
		"stronger, with the thickness of the air threatening to swallow me whole. It was like I had entered "
		"a world utterly surreal- foreign in every conceivable respect.")
	
	output("\n\"What I mean by that is, "
		"while I would delight in saying that the decision you made in coming here was a good one, "
		"and that the people within this realm will greet you with open arms...\"\n")
	
	output("\"Well... Let's just say we don't always get what we want... Wouldn't you agree?\"")
	
	output("\n\"...\"\n")
	
	output("\"Anyways, I'm sure you didn't come all this way just to listen to me ramble, "
	"and I'm sure you're eager to get on with this new era of your life.\"\n")
	
	name = getInput("\"But before you leave, I must know... What is your name?\" ")
	
	output("\n\"Alright then. Thank you " + name + ", you may go. And good luck. God only knows how much you will need it.\"\n")

def scene1():
	global name
	output("")

intro()