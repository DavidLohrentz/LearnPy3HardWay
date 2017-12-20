#!/bin/bash
dir=$(pwd -P)
sudo docker run -it --name learn-alpine --rm -v /any-directory-you-wish-to-copy:/var/opt alpine:3.6 /bin/sh
