#!/bin/bash
date=`date +%y%m%d`
mkdir -p ${USER}/${date}/

read -p "How many more files would you like to create?" fileCount

totalCount=0
if [ -e "${USER}/${date}/.totalCount" ] ; then
    totalCount=$(cat "${USER}/${date}/.totalCount")
fi

while [ $fileCount -gt 0 ] ; do
    touch "${USER}/${date}/${USER}_${totalCount}"
    fileCount=$((fileCount - 1))
    totalCount=$((totalCount + 1))
done

echo $totalCount > "${USER}/${date}/.totalCount"
