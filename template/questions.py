class Question:
    def __init__(self, q, a, points, hint, calc):
        self.q = q # question
        self.a = a # answer - if a number, round to two decimal places if necessary
        # NOTE: Answer can be integer, string, or list! (Capitalisation doesn't matter)

        self.points = points # points given if the question is answered correctly
        self.hint = hint # question hint
        self.calc = calc # True/False - allow or deny access to the inbuilt calc

ques = [
    Question("", "", 0, "", False), # Leave blank!!
    Question("", "", 0, "", False), #1 - Blank Template

    # example questions
    Question("Name a primary paint colour.", ["Red", "Yellow", "Blue"], 3, "Secondary Colours are Orange, Green, and Magenta.", False),
    Question("What is 3 + 3?", 6, 1, "3 + 3 = 1 + 1 + 1 + 1 + 1 + 1", True),
    Question("What is the capital of France?", "Paris", 2, "Eiffel Tower", False),

]
