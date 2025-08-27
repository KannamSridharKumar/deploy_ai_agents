#!/bin/bash

URL="http://0.0.0.0:8080/chat"

DATA='{
  "message": "Whats the status of the order with tracking ID T1234"
}'

curl -X POST \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d "$DATA" \
  "$URL"







