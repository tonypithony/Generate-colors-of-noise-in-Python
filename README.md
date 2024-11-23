![](https://raw.githubusercontent.com/tonypithony/Generate-colors-of-noise-in-Python/refs/heads/main/noizes.png)

![](https://raw.githubusercontent.com/tonypithony/Generate-colors-of-noise-in-Python/refs/heads/main/color-noize.png)

![](https://raw.githubusercontent.com/tonypithony/Generate-colors-of-noise-in-Python/refs/heads/main/spectrums.PNG)

# Sources
 
* [Generate colors of noise in Python](https://stackoverflow.com/questions/67085963/generate-colors-of-noise-in-python)
* [Функции шума и генерирование карт](https://habr.com/ru/articles/321874/)
* [Красный шум](https://ru.wikipedia.org/wiki/%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D1%8B%D0%B9_%D1%88%D1%83%D0%BC)
* [Анализ аудиоданных с помощью глубокого обучения и Python (часть 1)](https://nuancesprog.ru/p/6713/)

# Bonus №0

![](https://raw.githubusercontent.com/tonypithony/Generate-colors-of-noise-in-Python/refs/heads/main/dwt.PNG)

## Sources
* [Strikethrough rows and columns in matrices](https://tex.stackexchange.com/questions/235599/strikethrough-rows-and-columns-in-matrices)
* [Vertical line in matrix using LaTeXiT](https://tex.stackexchange.com/questions/33519/vertical-line-in-matrix-using-latexit)
* [Вейвлет-сжатие «на пальцах»](https://habr.com/ru/articles/168517/)
* [Сжатие изображений с потерями](https://habr.com/ru/articles/251417/)

# Bonus №1

![](https://raw.githubusercontent.com/tonypithony/Generate-colors-of-noise-in-Python/refs/heads/main/am.jpeg)

```python
import os
# Форсируем работу только на процессоре.
os.environ['CUDA_VISIBLE_DEVICES'] = ''
import tensorflow as tf 
```
 
```python
callbacks = [
    keras.callbacks.EarlyStopping(monitor="loss", min_delta=0.01, patience=2, verbose=1),
    keras.callbacks.ModelCheckpoint(filepath="mymodel_{epoch}", save_best_only=True, monitor="loss", verbose=1),
] 
```

## Sources

* [pip install tensorflow-cpu](https://pypi.org/project/tensorflow-cpu/)
* [Запуск TensorFlow на CPU вместо GPU без переписывания кода](https://sky.pro/wiki/python/zapusk-tensor-flow-na-cpu-vmesto-gpu-bez-perepisyvaniya-koda/)
* [Тонкая настройка и контроль процесса обучения через метод fit()](https://proproprogs.ru/tensorflow/keras-tonkaya-nastroyka-kontrol-processa-obucheniya-cherez-metod-fit)


# Bonus №2

```bash
#!/usr/bin/bash

# Для удаления старых ядер, кроме последнего и предпоследнего, можно использовать команду
sudo apt-get purge $(dpkg -l 'linux-*' | sed '/^ii/!d;/'"$(uname -r | sed "s/\(.*\)-\([^0-9]\+\)/\1/")"'/d;s/^[^ ]* [^ ]* \([^ ]*\).*/\1/;/[0-9]/!d' | head -n -1)

sudo apt-get autoclean

sudo apt-get autoremove
```

```bash
#!/bin/bash
set -eu
LANG=en_US.UTF-8 snap list --all | awk '/disabled/{print $1, $3}' |
while read snapname revision; do
snap remove "$snapname" --revision="$revision"
done

# удаление старых пакетов snap
```

```bash
#!/bin/bash

# Обновляем пакеты
sudo apt update
sudo apt upgrade -y

# Очищаем кэш
sudo apt autoclean
sudo apt autoremove -y

# Выводим сообщение об успешном завершении
echo "Система успешно обновлена"
```

## Sources

* [Основные команды очистки диска в Ubuntu](https://vmblog.ru/ochistka-diska-ubuntu-linux/)
* [Best Disk Analyzer Software for Linux](https://www.ubuntupit.com/best-disk-analyzer-tools-for-linux-system/)
* [Conky - мощный и легко настраиваемый системный монитор](https://help.ubuntu.ru/wiki/conky)
