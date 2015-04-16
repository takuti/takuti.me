#! /bin/sh

if [ $# -ne 2 ] ; then
  echo "error"
  exit 1
fi

BEFORE=$1
AFTER=$2

for FILE in ../_posts/*
do
    if grep -q "\- ${BEFORE}" ${FILE}
    then
      sed -i -n -e "s/\- ${BEFORE}/\- ${AFTER}/" ${FILE}
      echo "${FILE} : ${BEFORE}->${AFTER}"
    fi
done
