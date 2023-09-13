#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <text>"
  exit 1
fi

text="$1"
border=$(printf "+%*s+" "${#text}" "")

echo "$border"
echo "| $text |"
echo "$border"
