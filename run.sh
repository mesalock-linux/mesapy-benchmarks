#!/bin/bash -e

for f in "${@:2}"; do
    echo $f
    for i in {0..9}; do
        /usr/bin/time -f "%E" $1 $f > /dev/null
    done;
    echo ""
done;
