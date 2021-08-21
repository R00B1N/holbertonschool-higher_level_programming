#!/bin/bash
# a Bash script that displays only the status code
curl -s -w "%{http_code}" "$1" -o /dev/null
