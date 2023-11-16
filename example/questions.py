class Question:
    def __init__(self, q, a, points, hint, calc):
        self.q = q # question
        self.a = a # answer - if a number, round to two decimal places if necessary
        # NOTE: Answer can be integer, string, or list! (Capitalisation doesn't matter)

        self.points = points # points given if the question is answered correctly
        self.hint = hint # question hint
        self.calc = calc # True/False - allow or deny access to the inbuilt calc

ques = [
    Question("", "", 0, "", False), # Blank Template
    Question("Name a primary paint colour.", ["Red", "Yellow", "Blue"], 1, "Secondary Colours are Orange, Green, and Magenta", False), #1
    Question("What is 3 ^ 3?", 27, 2, "3 ^ 3 = 3 * 3 * 3", True), #2
    Question("What is the capital of France?", "Paris", 3, "Eiffel Tower", False),  #3
    Question("How long is 3 hours and 29 minutes in seconds?", 12540, 4, "There are 60 seconds in a minute, and 60 minutes in an hour", True), #4
    Question("What is the square root of 144?", 12, 5, "√100 = 10, and the √225 = 15", True), #5
    Question("What is the name of the world's largest ocean?", "Pacific", 6, "Australia and New Zealand are in this ocean", False), #6
    Question("In the story of Snow White, how many dwarfs are there?", 7, 2, "Four of them are Dopey, Doc, Bashful, and Sneezy...", False), #7
    Question("What is the chemical symbol for gold?", "Au", 8, "It's a two-letter symbol", False), #8
    Question("What is the maximum number of players on a standard soccer team?", 11, 4, "It's a prime number", False), #9
    Question("Which planet is known as the 'Red Planet'?", "Mars", 5, "It's the fourth planet from the sun", False), #10
    Question("What is the largest country in the world?", "Russia", 3, "It's in Europe", False), #11
    Question("How many time zones does Russia span?", 11, 7, "It's in the double digits!", False), #12
    Question("In which year did the first modern Olympic Games take place?", 1896, 6, "It's in the 19th century", False), #13
    Question("What Shakespeare play is the quote 'To be or not to be' from?", "Hamlet", 7, "It's a tragedy", False), #14
    Question("What is the name of the main African country in 'Black Panther'?", "Wakanda", 5, "It's a made-up country", False), #15
    Question("In what year did The Beatles release their first album?", 1963, 7, "It's in the 20th century", False), #16
    Question("What is the largest bird in the world?", "Ostrich", 3, "It's a flightless bird", False), #17
    Question("What is x equal to? 2x + 5 = 11", 3, 4, "It's a prime number", True), #18
    Question("What is the name of the main character in 'The Hobbit'?", "Bilbo Baggins", 6, "It's a fantasy book", False), #19
    Question("What is the name of the largest known moon in our solar system?", "Ganymede", 8, "It's a moon of Jupiter", False), #20
    Question("What is the smalled prime number, which is also a palindrome?", 101, 5, "It's a 3-digit number", True), #21
    Question("What is the chemical formula for laughing gas? (e.g. H2O)", "N2O", 6, "It's a two-letter symbol", False), #22

    # at this point, the questions just become stupidly difficult
    Question("In astronomy, what is the name of the point in the sky directly above an observer and opposite the zenith?", "Nadir", 14, "It's a 5-letter word", False), #23
    Question("What is the term for a polygon with 1,000 sides?", "Chiliagon", 12, "It's a 9-letter word", False), #24
    Question("In biology, what is the term for the phenomenon where an organism can reproduce without the involvement of another organism?", "Parthenogenesis", 15, "It's a 15-letter word", False), #25
    Question("What is the value of the mathematical constant known as the golden ratio, often denoted by the Greek letter phi (φ) - to 2 decimal places?", 1.62, 10, "The number lies between 1 and 2", True), #26
    Question("What is the term for a style of architecture and art that emerged in Italy in the late 16th century, characterized by ornate decoration and dramatic effects?", "Baroque", 9, "The word means 'irregularly shaped'", False), #27
    Question("What is the name of the largest known star in the universe?", "UY Scuti", 13, "It's a 2-word name", False), #28
    Question("In chemistry, what is the term for a reaction where one substance is both oxidized and reduced?", "Disproportionation", 16, "It's a 16-letter word", False), #29
    Question("What is the term for a complex mathematical structure that is a higher-dimensional analog of a torus?", ["Tesseract", "Hypercube"], 17, "There are two names for it (you only have to give one)", False), #30
]
