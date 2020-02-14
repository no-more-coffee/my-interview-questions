VOWELS = "aeiou"


class Interlocutor:
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def connect(self, chat):
        self.chat: Chat = chat

    def send(self, message):
        self.chat.send(self.name, message)


class Human(Interlocutor):
    pass


class Robot(Human):
    pass


def to_binary(message):
    return ''.join("0" if m in VOWELS else "1" for m in message.lower())


class Chat:
    def __init__(self) -> None:
        super().__init__()
        self.dialogue = []

    def show_human_dialogue(self):
        return f'\n'.join(
            fr"{name} said: {message}"
            for name, message in self.dialogue
        )

    def show_robot_dialogue(self):
        return f'\n'.join(
            fr"{name} said: {to_binary(message)}"
            for name, message in self.dialogue
        )

    def connect_human(self, human):
        human.connect(self)

    def connect_robot(self, robot):
        robot.connect(self)

    def send(self, name, message):
        self.dialogue.append((name, message))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chat = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    assert chat.show_human_dialogue() == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
    assert chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""

    print("Coding complete? Let's try tests!")
