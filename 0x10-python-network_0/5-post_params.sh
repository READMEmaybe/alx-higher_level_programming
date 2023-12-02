#!/bin/bash
# This script will display the body of the response with parameters
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
