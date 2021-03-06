#!/bin/bash

GEN_CMD="./closure -generate"
NLIN_CL_CMD="./closure -naive - 0"
LIN_CL_CMD="./closure -improved - 0"

TIMEFORMAT=%R;
echo -e "# \t nlin \t lin" 
n=5;
for i in `seq 100 100 5000`; do
  for j in `seq 1 $n`; do
      nlin_time=$( $GEN_CMD $i | { time  $NLIN_CL_CMD > /dev/null; } 2>&1)
	  lin_time=$( $GEN_CMD $i | { time $LIN_CL_CMD > /dev/null; } 2>&1)
    echo -e "$i \t $nlin_time \t $lin_time" 
  done
done
