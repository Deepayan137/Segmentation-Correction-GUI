#!/usr/bin/python

tempFolder=$1 #path of temporary folder where images from the web portal will be saved and also it will contain the text files
skewtempFolder=$2 #path of tempoary folder that will conatin the skewed images

python gui.py $tempFolder $skewtempFolder
