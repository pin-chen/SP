#!/bin/bash

ctfd='ctfd_7de27241ac3ecd3a9ad87ae1e9c82142116abae3a54ff1a50e331fcfe1163c69'

website=$(curl -X POST -d "token=$ctfd&recreate=on" http://10.105.0.21:22000/  | grep -o 'http://[^<]*' | sed 's/<\/code>//')

#website='http://10.105.0.21:11358'

echo $website

sleep 3