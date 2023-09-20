grep -v '^#' /etc/protocols | awk '{print $1, $2}' | sort -k2 -n -r | head -n 5
