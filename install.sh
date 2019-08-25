#!/bin/bash

for filename in manifests/*.mnfs; do
    ./manifesto -o ${filename%.mnfs}.mnfb $filename
done

cp ./insclick /usr/bin/
cp ./rmclick /usr/bin/
cp ./manifesto /usr/bin/
mkdir -p "/opt/manifesto/manifests"
cp ./*.json /opt/manifesto/
cp  ./manifests/*.mnfb /opt/manifesto/manifests