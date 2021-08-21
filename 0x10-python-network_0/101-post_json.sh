
#!/bin/bash
# a Bash script that sends a JSON POST request, JSON file is passed as arg
curl -s -X POST -H "Content-Type: application/json" "$1" -d @"$2"
