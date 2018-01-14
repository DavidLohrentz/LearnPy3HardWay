#!/bin/bash
dir=$(pwd -P)
sudo docker run -it --name learn-p --rm -v $dir:/var/opt python:3.7-rc-alpine /bin/sh
