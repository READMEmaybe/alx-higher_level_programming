#!/bin/bash
# This script will only dsiplay the status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
