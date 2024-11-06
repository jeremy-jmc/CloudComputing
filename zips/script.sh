#!/bin/bash

mkdir -p unzipped
for zip_file in *.zip; do
  echo "Descomprimiendo $zip_file en unzipped/"
  unzip "$zip_file" -d "unzipped/${zip_file%.zip}/"
done