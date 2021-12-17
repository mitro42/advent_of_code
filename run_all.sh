source ~/.virtualenvs/aoc/bin/activate
find  -mindepth 2 -name \*.py  | sort | xargs -I {} bash -c "echo {}; python {}; echo ---"