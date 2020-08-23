#!/bin/bash
#Nier Installation Clone: https://www.youtube.com/watch?v=AczZoNeso04

#Resetting Invalid to 0 incase script has been uncleanly exited before..
INVALID=0

#Will Question
function will {
clear
invalid
echo 'LOADING - CHECKING SYSTEM...'
echo ' '
echo 'Will. From where does our will come?'
echo '1. It is born from nothingness.'
echo '2. It is given to us by God.'
echo '3. I dont care. I dont need any of this!'
read -n 1 -p "Please select 1, 2 or 3." answer
	if [ "$answer" = "1" ]; then
		nothingness
	elif [ "$answer" = "2" ]; then
		god
	elif [ "$answer" = "3" ]; then
		care
	else 
		INVALID=1
		will
	fi 
}

#Nothingness Question
function nothingness {
clear
invalid
echo 'LOADING - CHECKING SYSTEM...'
echo ' '
echo 'Nothingness. Is there any meaning to living in this world?'
echo '1. Pray to God.'
echo '2. Hold true to your own will.'
echo '3. I dont care. I dont need any of this!'
read -n 1 -p "Please select 1, 2 or 3." answer
	if [ "$answer" = "1" ]; then
		god
	elif [ "$answer" = "2" ]; then
		will
	elif [ "$answer" = "3" ]; then
		care
	else
		INVALID=1
		nothingness
	fi
}

#God Question
function god {
clear
invalid
echo 'LOADING - CHECKING SYSTEM...'
echo ' '
echo 'God. How did God create us?'
echo '1. By random chance.'
echo '2. From nothingness.'
echo '3. I dont care. I dont need any of this!'
read -n 1 -p "Please select 1, 2 or 3." answer
	if [ "$answer" = "1" ]; then
		chance
	elif [ "$answer" = "2" ]; then
		nothingness
	elif [ "$answer" = "3" ]; then
		care
	else
		INVALID=1
		god
	fi
}

#Chance question
function chance {
clear 
invalid
echo 'LOADING - CHECKING SYSTEM...'
echo ' '
echo 'Chance. Was this world created by random chance?'
echo '1. All is according to Gods will.'
echo '2. It was not random. This world is filled with nothingness.'
echo '3. I dont care. I dont need any of this!'
read -n 1 -p "Please select 1, 2 or 3." answer
	if [ "$answer" = "1" ]; then
		god
	elif [ "$answer" = "2" ]; then
		nothingness
	elif [ "$answer" = "3" ]; then
		care
	else
		INVALID=1
		chance
	fi
}

#Exit/care question
function care {
clear
invalid
echo 'LOADING - CHECKING SYSTEM...'
echo ' '
echo 'The game is currently being installed.'
echo 'You cannot continue playing the game until the install is completed.'
echo 'Do you wish to discard everything and return to the title screen?'
echo 'If you do, you will lose any unsaved data'
read -n 1 -p "y or n?" answer
	if [ "${answer,,}" = "y" ]; then
		clear
		echo 'Thank you for playing'
		sleep 1
		clear
		exit
	elif [ "${answer,,}" = "n" ]; then
		will
	else
		INVALID=1
		care
	fi
}

function invalid {
if [ "$INVALID" = "1" ]; then
	echo Invalid. Please try again.
	INVALID=0
fi
}

#Start Script from Will question
will
