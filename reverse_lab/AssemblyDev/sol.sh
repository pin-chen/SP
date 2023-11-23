#!/bin/bash
p1=`cat p1.asm | base64 -w0`
p2=`cat p2.asm | base64 -w0`
p3=`cat p3.asm | base64 -w0`
printf "$p1\n$p2\n$p3\n" | nc edu-ctf.zoolab.org 10020