#!/usr/bin/env bash

VAR1=$OUTFILE".out"
echo $VAR1
VAR2=$OUTFILE".err"
echo $VAR2
./cmd1 < $INFILE | ./cmd3 > $VAR1 2> $VAR2