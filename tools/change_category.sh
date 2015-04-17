#! /bin/sh

BEFORE="http:\/\/blog.takuti.me\/images\/wp"
AFTER="\/images\/wp"

for FILE in ../_posts/*
do
    if grep -q "${BEFORE}" ${FILE}
    then
      sed -i -n -e "s/${BEFORE}/${AFTER}/" ${FILE}
      echo "${FILE} : ${BEFORE}->${AFTER}"
    fi
done
