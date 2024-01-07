#!/bin/bash

ctfd='ctfd_7de27241ac3ecd3a9ad87ae1e9c82142116abae3a54ff1a50e331fcfe1163c69'

echo $(curl -X POST -d "token=$ctfd&recreate=on" http://chal1.eof.ais3.org:12000/)