#!/bin/bash
git add --all *
git commit -am "commit at $(date +%Y%m%d%H%M%S)"
git push -u origin master
