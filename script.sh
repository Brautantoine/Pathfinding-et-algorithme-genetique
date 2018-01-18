#!/bin/bash

clear
for i in {1..10}
do
	python testVille.py | cowsay -W120
done
exit 0
