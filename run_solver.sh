#!/bin/sh

for f in tests/unencoded/*
do
	python sudokusolver.py encode $f
	minisatinput="tests/encoded/"$(basename $f)
	minisatoutput="tests/decode/"$(basename $f)
	minisat $minisatinput $minisatoutput 
	python sudokusolver.py decode $minisatoutput
	echo "\n\n"
done
