#!/bin/bash

export PYPHI_WELCOME_OFF='yes'

for graph in $(ls graphs); do
  echo "----------"
  echo $graph
  python graphs/$graph
done
