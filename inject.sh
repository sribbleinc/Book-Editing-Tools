#!/bin/bash
vars=$(cat vars.txt)
target=$(pwd)
#Windows Hack; if you're home directory isn't C: you're smart enough to modify the script.
if [[ $target == /C:* ]]; then
    target=$(echo $target | cut -d: -f2-)
elif [[ $target == /mnt/c* ]]; then
    target=$(echo $target | cut -dc -f2-)
fi
cp comicautoformat_template.py comicautoformat.py
perl -i -pe "s|REPLACE|$vars|" comicautoformat.py
perl -i -pe "s|_target_|$target|" comicautoformat.py
