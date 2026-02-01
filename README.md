# TermiGotchi

## The Friendly Terminal Friend

A virtual pet that lives in your terminal! TermiGotchi runs as a background server and will notify you when your pet needs attention while you work.

## Quick Start

### 1. Start the TermiGotchi Server

```bash
python3 termi.py
```

The server will run in the background, and your pet will start living its life. You'll get notifications when it needs attention.

### 2. Interact with Your Pet

**Interactive mode:**
```bash
python3 termi_client.py
```

**Quick status check:**
```bash
./check_pet.sh
# or
python3 termi_client.py status
```

**Single commands:**
```bash
python3 termi_client.py feed
python3 termi_client.py play
python3 termi_client.py fun
```

## Available Commands

- `status` - Check your pet's current status and mood
- `feed` - Feed your pet (reduces appetite)
- `play` - Play with your pet (reduces boredom)
- `fun` - Take your pet out for fun (reduces boredom)

## How It Works

Your TermiGotchi lives on a socket server (port 61420) and continuously simulates life:
- Appetite and boredom increase over time
- Mood changes based on current stats
- The pet will notify you when it needs attention
- You can interact with it using the client while working in your terminal

## Requirements

- Python 3.13.3 (or compatible version)
- No external dependencies - uses only Python standard library

## Pet Stats

- **Level** - Your pet's current level
- **Health** - Physical wellbeing
- **Mana** - Energy level
- **Appetite** - How hungry your pet is (keep this low!)
- **Boredom** - How bored your pet is (keep this low!)
- **Mood** - Emotional state (very_good, good, normal, not_good, bad, really_bad, sick)
