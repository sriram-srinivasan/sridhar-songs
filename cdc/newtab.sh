#!/bin/sh
perl -i -pe 's/<a xl:href/<a target="_blank" xl:href/g' *.svg
perl -i -pe 's/^.*<title>.*1<\/title>.*$//' *.svg

