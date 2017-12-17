#!/bin/bash
dir=$(pwd -P)
sudo docker run -it --name learn-p --rm -v $dir:/var/opt python:3.6.3-alpine3.6 /bin/sh
