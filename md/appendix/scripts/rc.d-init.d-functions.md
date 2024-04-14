# /etc/rc.d/init.d/functions

Общие функции для скриптов системы инициализации (`startup`, `shutdown`, загрузочные скрипты). Сейчас там расположены только функции для печати сообщений в терминал.

## Что делает скрипт

Объявляет функции `print_msg` и `check_status`.

## Листинг

```bash
#!/bin/ash
# Shared functions and variables
# (C) 2024 mskrasnov <https://github.com/mskrasnov>

function print_msg() {
  echo -ne "[ \e[1;33m***\e[0m ] $1 "
}

function check_status() {
  local ERR=$?
  if [ $ERR -eq 0 ]; then
    echo -e "[ \e[32mOK\e[0m ]"
  else
    echo -e "[\e[31mERRR\e[0m] (code: $ERR)"
  fi
}
```
