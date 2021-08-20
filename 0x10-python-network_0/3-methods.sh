#!/bin/bash
# a Bash script that displays all HTTP methods the server will accept
curl -s -I "$1" | grep "Allow" | cut -d " " -f 2-
