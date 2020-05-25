#!/bin/bash

for filename in manifests/*.mnfs; do
    ./manifesto -i $filename
done

#cp ./manifesto /usr/bin/
#mkdir -p "/opt/manifesto/manifests"
#cp  ./manifests/*.mnfb /opt/manifesto/manifests