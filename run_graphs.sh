#!/bin/bash

export PYPHI_WELCOME_OFF='yes'

for graph in $(ls graphs); do
  echo "----------" >>results_sh.txt
  echo $graph >>results_sh.txt
  python graphs/$graph >>results_sh.txt
done
