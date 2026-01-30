import enum
import time

class Mood(enum.Enum):
    very_good = 0
    good = 1
    normal = 2
    not_good = 3
    bad = 4
    really_bad = 5
    sick = 6


class PetStatus:
    level: int
    health: int
    mana: int
    appetite: int
    bored: int
    mood: Mood

    def __init__(self, level, health, mana, appetite, bored):
        self.level = level
        self.health = health
        self.mana = mana
        self.appetite = appetite
        self.bored = bored
        self.mood = Mood.good

    def print(self):
        print(self.__str__())

    def __str__(self):
        ret_str = "Level: {level}\nHealth: {health}\nMana: {mana}\nAppetite: {appetite}\nBored: {bored}\n"
        return ret_str.format(level = str(self.level), health = str(self.health), mana = str(self.mana), appetite = str(self.appetite), bored = str(self.bored))

    def calc_mood_count(self):
        sum = (10 * health + 8 * appettite + 5 * bored) / 10
        return sum 

    def set_mood(self):
        mood_count = 0.0
        mood_count = calc_mood_count()

        if mood_count == 0.0 and mood_count < 10:
            self.mood = Mood.really_bad
        elif mood_count >= 10 and mood_count < 20:
            self.mood = Mood.bad
        elif mood_count >= 20 and mood_count < 20:
            self.mood = Mood.not_good
        elif mood_count >= 30 and mood_count < 20:
            self.mood = Mood.normal
        elif mood_count >= 40 and mood_count < 20:
            self.mood = Mood.good
        elif mood_count >= 50 and mood_count < 20:
            self.mood = Mood.very_good

    def get_mood(self):
        return self.mood.name


class TermiGotchi:
    name: str
    status: PetStatus(0, 10, 0, 0, 0)

    def print_mood(self):
        print("My current mood is: " + self.status.get_mood())

    def print(self):
        print("Hello I am " + self.name)
        print("My current status:\n" + self.status.__str__())

    def __init__(self, name, status):
        self.name = name
        self.status = status

    def play(self):
        if self.status.bored > 0:
            self.status.bored -= 1

    def eat(self):
        if self.status.appetite > 0:
            self.status.appetite -= 1

    def go_out(self):
        if self.status.bored > 0:
            self.status.bored -= 1

    def live(self):
        wlen = random.random()
        sleep(wlen) # Emulate doing some work
        value = random.randrange(1, 50)
        sleep(wlen) # Emulate doing some work
        situation = random.randrange(1, 10)

        if 1 or 3 or 5 or 7 or 9:
            self.status.appetite += value
        else:
            self.status.bored += value

        if self.status.appetite > 0 and self.status.appetite < 10:
            self.status.mood = Mood.normal
        elif slef.status.appetite >= 10 and self.status.appetite < 20:
            self.status.mood = Mood.not_good
        print('work done in %0.2f seconds' % wlen)

def main() -> None:
    currentStatus = PetStatus(0, 10, 0, 0, 0)
    termiGotchi = TermiGotchi("Joe", currentStatus)


    print("Termi Gotchi Class")
    termiGotchi.print()
    while 1:
        t = threading.Thread(target=termiGotchi.live())
        time.sleep(4)


if __name__ == '__main__':
    main()
