class Greetings:
    def __init__(self, name, hour):
        self.name = name
        self.hour = hour

    def sayName(self):
        print("Hello {}".format(self.name))

greet = Greetings('Drex', 12)
greet.sayName()
