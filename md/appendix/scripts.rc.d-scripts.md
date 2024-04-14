# /etc/rc.d/init.d/scripts/

Скрипты в этой директории запускают конкретные системные компоненты (обычные программы или демоны). Содержат команды для запуска, остановки и перезапуска этих компонентов.

## Использование

`/etc/rc.d/init.d/scripts/SCRIPT_NAME {start|stop|restart}`

- `start` — запустить скрипт;
- `stop` — остановить скрипт;
- `restart` (опционально) — перезапустить скрипт.

## Листинг

Рассмотрим на примере `/etc/rc.d/init.d/scripts/syslog.sh`:

```bash
#!/bin/ash
# (C) 2024 mskrasnov <https://github.com/mskrasnov>

. /etc/rc.d/init.d/functions

SYSLOG_ROT_SIZE=65536

case $1 in
  start)
    print_msg "Starting syslog..."
    syslogd -m 0 -s $SYSLOG_ROT_SIZE -L
    check_status

    print_msg "Starting klogd..."
    klogd
    check_status
  ;;

  stop)
    print_msg "Stopping klogd..."
    killall klogd
    check_status

    print_msg "Stopping syslogd..."
    killall syslogd
    check_status
  ;;

  restart)
    $0 stop
    $0 start
  ;;

  *)
    echo "Usage: $0 {start|stop|restart}"
    exit 1
  ;;
esac
```
