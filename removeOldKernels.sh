#!/usr/bin/bash

# Для удаления старых ядер, кроме последнего и предпоследнего, можно использовать команду
sudo apt-get purge $(dpkg -l 'linux-*' | sed '/^ii/!d;/'"$(uname -r | sed "s/\(.*\)-\([^0-9]\+\)/\1/")"'/d;s/^[^ ]* [^ ]* \([^ ]*\).*/\1/;/[0-9]/!d' | head -n -1)

sudo apt-get autoclean

sudo apt-get autoremove