#!/bin/bash

for filename in manifests/*.mnfs; do
    ./manifesto -o ${filename%.mnfs}.mnfb $filename
done

cp ./insclick /usr/bin/
cp ./rmclick /usr/bin/
cp ./manifesto /usr/bin/
