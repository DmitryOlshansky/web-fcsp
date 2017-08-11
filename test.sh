#!/bin/sh

testrest(){
	if [ "x$1" != "x$2" ] ; then 
		echo "FAILED. $1 vs $2"
		exit 1
	fi	
}

# single mol
testrest "\"6,00\"" `http -f POST localhost:5000/encode_one file@FCSS/1.MOL | jq ".code"`

# multiple mol
TEMP=`mktemp`
http -f POST localhost:5000/encode_many file1@FCSS/1.MOL file2@FCSS/2.MOL > $TEMP
testrest "\"6,00\"" `cat $TEMP | jq ".file1.code"`
testrest "\"3,00\"" `cat $TEMP | jq ".file2.code"`
