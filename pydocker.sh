#!/bin/bash
dir=$(pwd -P)
sudo docker run -it --name learn-p --rm -v $dir:/var/opt python:3.6.4-alpine3.7 /bin/sh
