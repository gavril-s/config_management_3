#!/bin/bash

text="$1"
border=$(printf "+%-*s+" "${#text}" "")

echo "$border"
echo "| $text |"
echo "$border"
