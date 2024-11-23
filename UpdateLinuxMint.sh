#!/bin/bash

# Обновляем пакеты
sudo apt update
sudo apt upgrade -y

# Очищаем кэш
sudo apt autoclean
sudo apt autoremove -y

# Выводим сообщение об успешном завершении
echo "Система успешно обновлена"