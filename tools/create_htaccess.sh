#! /bin/sh

echo '' > .htaccess

for FILE in ../_posts/*
do
  if [[ ${FILE} =~ ^../_posts/([0-9]{4})-([0-9]{2})-([0-9]{2})-([0-9a-zA-Z\-]+).*$ ]] ; then # ex) _posts/2013-10-27-time-capsule.html
    echo "Redirect 301 /${BASH_REMATCH[4]}/ /${BASH_REMATCH[1]}/${BASH_REMATCH[2]}/${BASH_REMATCH[4]}/" >> .htaccess
  fi
done

