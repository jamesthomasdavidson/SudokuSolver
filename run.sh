#!/bin/sh

for f in tests/unencoded/*
do
	minisatinput="tests/encoded/"$(basename $f)
	minisatoutput="tests/decode/"$(basename $f)
	python sudokusolver.py encode $f $minisatinput
	minisat $minisatinput $minisatoutput 
	python sudokusolver.py decode $minisatoutput
	echo "\n\n"
done
