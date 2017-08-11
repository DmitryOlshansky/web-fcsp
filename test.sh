#!/bin/sh

testrest(){
	if [ "x$1" != "x$2" ] ; then 
		echo "FAILED. $1 vs $2"
		exit 1
	fi	
}

testrest "\"6,00\"" `http -f POST localhost:5000/encode_one file@FCSS/1.MOL | jq ".[0].code"`
