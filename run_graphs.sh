#!/bin/bash

for graph in $(ls graphs); do
  echo "----------"
  echo $graph
  python graphs/$graph
done
