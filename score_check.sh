#!/bin/bash
for i in $(find /proc -maxdepth 1 -type d); do

if [ -f "$i"/oom_score ]; then
  printf "$(cat "$i"/oom_score) ";
  pid=$(echo "$i" | awk -F'/' '{print $3}';)
    if [ "$(cat "$i"/oom_score)" -ge 1 ];then
      printf  "$(ps -p "$pid" -o comm=) ";
    fi
  printf "$i/oom_score \n";
fi;

done | awk '$1 > 1' | sort -n -k1
