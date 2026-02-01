#!/bin/bash
# Quick script to check your TermiGotchi's status
python3 "$(dirname "$0")/termi_client.py" status
