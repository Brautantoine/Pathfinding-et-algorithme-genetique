#/bin/bash

DATE='/bin/date'

BEFORE=$($DATE +'%s')

clear

python testVille.py | cowsay -W120 -e "><"

AFTER=$($DATE +'%s')

ELAPSED=$(($AFTER - $BEFORE))

echo "Temps d'execution :"  $ELAPSED  "secondes"

exit 0
