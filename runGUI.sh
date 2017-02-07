#!/usr/bin/python
mkdir ~/temp1 ~/temp2
#temp1=$1 #path of temporary folder where images from the web portal will be saved and also it will contain the text files
#temp2=$2 #path of tempoary folder that will conatin the skewed images

#python gui.py $tempFolder $skewtempFolder
python gui.py ~/temp1/ ~/temp2/

rm -rf ~/temp1 ~/temp2