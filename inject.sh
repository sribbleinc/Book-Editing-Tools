#!/bin/bash
vars=$(cat vars.txt)
target=$(pwd)
cp comicautoformat_template.py comicautoformat.py
perl -i -pe "s|REPLACE|$vars|" comicautoformat.py
perl -i -pe "s|_target_|$target|" comicautoformat.py
