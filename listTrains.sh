#!/usr/bin/env bash

for train in "$(find . -iname 'train*' -type d)"; do

  train_name="$(basename ${train})"
  echo "registry:5000/${train_name}"
done
