#!/usr/bin/env python3
"""
TermiGotchi Client - Interact with your virtual pet
"""
import socket
import sys

def send_command(command):
    """Send a command to the TermiGotchi server and print response"""
    host = '127.0.0.1'
    port = 61420
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(command.encode())
            response = s.recv(4096).decode()
            print(response)
    except ConnectionRefusedError:
        print("❌ Cannot connect to TermiGotchi server!")
        print("Make sure the server is running: python3 termi.py")
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) > 1:
        # Command provided as argument
        command = sys.argv[1]
        send_command(command)
    else:
        # Interactive mode
        print("=" * 50)
        print("TermiGotchi Client - Interactive Mode")
        print("=" * 50)
        print("\nAvailable commands:")
        print("  status - Check your pet's status")
        print("  feed   - Feed your pet (reduces appetite)")
        print("  play   - Play with your pet (reduces boredom)")
        print("  fun    - Take your pet out for fun (reduces boredom)")
        print("  quit   - Exit client")
        print("=" * 50 + "\n")
        
        while True:
            try:
                command = input("🐾 Command: ").strip().lower()
                
                if command == 'quit' or command == 'exit':
                    print("Goodbye! 👋")
                    break
                elif command in ['status', 'feed', 'play', 'fun']:
                    send_command(command)
                elif command == '':
                    continue
                else:
                    print("Unknown command. Try: status, feed, play, fun")
            except KeyboardInterrupt:
                print("\n\nGoodbye! 👋")
                break
            except EOFError:
                break

if __name__ == '__main__':
    main()
