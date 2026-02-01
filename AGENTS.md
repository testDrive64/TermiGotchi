# AGENTS.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

TermiGotchi is a virtual pet simulation that runs in the terminal. It uses a socket-based architecture where the pet lives on a server and users interact with it through socket connections.

## Architecture

### Core Components

- **PetStatus**: Tracks pet attributes (level, health, mana, appetite, boredom) and calculates mood based on these stats. Includes `calc_mood_count()` for mood calculation and `set_mood()` for updating mood state.
- **Mood**: Enum defining pet emotional states from `very_good` to `sick`
- **TermiGotchi**: Main pet class that owns a PetStatus and responds to user interactions (play, eat, go_out)
- **Socket Server**: Multi-threaded server on port 61420 that accepts multiple concurrent client connections
- **Life Simulation Thread**: Background daemon thread that runs `TermiGotchi.live()` every 10 seconds, prints notifications when pet needs attention

### Key Design Patterns

**Threading Model:**
- Main thread: Accepts incoming client connections
- Life simulation thread: Daemon thread that continuously updates pet state
- Client handler threads: One per connected client, handles command processing

**Life Simulation:**
The `TermiGotchi.live()` method:
1. Randomly increases appetite or boredom (value 1-4)
2. Updates mood based on current stats
3. Returns True if pet needs attention (appetite >= 20 or boredom >= 20)

## Running the Application

### Start the Server
```bash
python3 termi.py
```

The server binds to `127.0.0.1:61420` and:
- Starts a background life simulation thread
- Accepts multiple concurrent client connections
- Prints notifications when pet needs attention

### Interact with Your Pet

**Interactive mode:**
```bash
python3 termi_client.py
```

**Quick commands:**
```bash
python3 termi_client.py status
python3 termi_client.py feed
python3 termi_client.py play
python3 termi_client.py fun
./check_pet.sh  # Quick status check
```

### Available Commands

- `status` - Returns pet name, full status, and current mood
- `feed` - Reduces appetite via eat()
- `play` - Reduces boredom via play()
- `fun` - Reduces boredom via go_out()

## Files

- `termi.py` - Main server with TermiGotchi, PetStatus classes and socket server
- `termi_client.py` - Client script for interacting with the pet (interactive or single command)
- `check_pet.sh` - Convenience script for quick status check

## Development Context

- Python 3.13.3
- No external dependencies (uses only standard library: enum, random, socket, time)
- No test framework currently configured
- Currently on branch: `termi-pet-class`
