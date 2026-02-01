from enum import Enum
import random
import socket
import time
import threading
import select

class Mood(Enum):
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
        sum = (10 * self.health + 8 * self.appetite + 5 * self.bored) / 10
        return sum

    def set_mood(self):
        mood_count = 0.0
        mood_count = self.calc_mood_count()

        if mood_count >= 0.0 and mood_count < 10:
            self.mood = Mood.really_bad
        elif mood_count >= 10 and mood_count < 20:
            self.mood = Mood.bad
        elif mood_count >= 20 and mood_count < 30:
            self.mood = Mood.not_good
        elif mood_count >= 30 and mood_count < 40:
            self.mood = Mood.normal
        elif mood_count >= 40 and mood_count < 50:
            self.mood = Mood.good
        elif mood_count >= 50:
            self.mood = Mood.very_good

    def get_mood(self) -> Mood:
        return self.mood.name


class TermiGotchi:
    name: str
    status: PetStatus
    
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def print_mood(self):
        print("My current mood is: " + self.status.get_mood())

    def print(self):
        print("Hello I am " + self.name)
        print("My current status:\n" + self.status.__str__())

    def get_statics(self) -> str:
        return(self.status.__str__())

    def play(self):
        if self.status.bored > 0:
            self.status.bored -= 1

    def eat(self):
        if self.status.appetite > 0:
            self.status.appetite -= 1

    def go_out(self):
        if self.status.bored > 0:
            self.status.bored -= 1

    def live(self) -> None:
        value = random.randrange(1, 5)
        situation = random.randrange(1, 10)

        if situation in [1, 3, 5, 7, 9]:
            self.status.appetite += value
        else:
            self.status.bored += value

        # Update mood based on status
        self.status.set_mood()
        
        # Check if pet needs attention
        if self.status.appetite >= 20 or self.status.bored >= 20:
            return True  # Needs attention
        return False



def handle_client(conn, address, termiGotchi):
    """Handle individual client connection"""
    try:
        while True:
            data = conn.recv(1024).decode().strip()

            if not data:
                break

            print(f"Command from {address}: {data}")
            
            if data == 'status':
                response = f"Hello! I am {termiGotchi.name}\n{termiGotchi.get_statics()}Mood: {termiGotchi.status.get_mood()}\n"
            elif data == 'fun':
                termiGotchi.go_out()
                response = "Went out for fun! Boredom decreased.\n" + termiGotchi.get_statics()
            elif data == 'play':
                termiGotchi.play()
                response = "Played! Boredom decreased.\n" + termiGotchi.get_statics()
            elif data == 'feed':
                termiGotchi.eat()
                response = "Fed! Appetite decreased.\n" + termiGotchi.get_statics()
            else:
                response = "Unknown command. Available: status, fun, play, feed\n"
            
            conn.send(response.encode())
    except Exception as e:
        print(f"Error handling client {address}: {e}")
    finally:
        conn.close()
        print(f"Connection closed: {address}")


def life_simulation(termiGotchi):
    """Background thread that simulates the pet's life"""
    while True:
        time.sleep(10)  # Update every 10 seconds
        needs_attention = termiGotchi.live()
        
        if needs_attention:
            print(f"\n🐾 {termiGotchi.name} needs attention!")
            print(f"   Mood: {termiGotchi.status.get_mood()}")
            print(f"   Appetite: {termiGotchi.status.appetite}, Boredom: {termiGotchi.status.bored}")
            print(f"   Run 'python3 termi_client.py' to interact!\n")


def main() -> None:
    host = '127.0.0.1'  # Use localhost for easier connection
    port = 61420

    currentStatus = PetStatus(0, 10, 0, 0, 0)
    termiGotchi = TermiGotchi("Joe", currentStatus)
    
    print("="*50)
    print("TermiGotchi Server Starting!")
    print("="*50)
    termiGotchi.print()
    print(f"\nListening on {host}:{port}")
    print("Connect using: python3 termi_client.py")
    print("="*50 + "\n")

    # Start life simulation in background thread
    life_thread = threading.Thread(target=life_simulation, args=(termiGotchi,), daemon=True)
    life_thread.start()

    termi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    termi_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    termi_socket.bind((host, port))
    termi_socket.listen(5)

    try:
        while True:
            conn, address = termi_socket.accept()
            print(f"New connection from: {address}")
            # Handle each client in a separate thread
            client_thread = threading.Thread(target=handle_client, args=(conn, address, termiGotchi))
            client_thread.start()
    except KeyboardInterrupt:
        print("\n\nShutting down TermiGotchi server...")
    finally:
        termi_socket.close()


if __name__ == '__main__':
    main()
