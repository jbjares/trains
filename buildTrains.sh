#!/usr/bin/env bash

for train in "$(find . -iname 'train*' -type d)"; do

  train_name="$(basename ${train})"

  # Build the train and tag with the local registry
  cd $train
    docker build --rm --no-cache --pull -t "${train_name}" .
    docker tag "${train_name}" "registry:5000/${train_name}"
  cd ..
done
