from mycroft import MycroftSkill, intent_file_handler

class SMathSkill(MycroftSkill):
    def __init__(self):
        super().__init__()

    @intent_handler('smath.intent')
    def handle_operation(self, message):
        operator = message.data.get('operator')
	n1 = message.data.get('number')
	n2 = message.data.get('number')
	if operator is not None:
		if operator == "plus" or operator == "add" or operator == "added to":
			n3 = n1 + n2
		if operator == "minus" or operator == "subtract":
			n3 = n1 - n2
		elif operator == "subtracted from":
			n3 = n2 - n1
		if operator == "multiply" or operator == "times" or operator == "multiplied by":
			n3 = n1 * n2
		if operator == "divide" or operator == "over" or operator == "divided by":
			n3 = n1 / n2
		self.speak_(n3)

    def stop(self):
        pass

def create_skill():
    return SMathSkill()

