# /etc/rc.d/shutdown

`/sbin/init` исполняет этот скрипт для выключения системы.

## Что делает скрипт

1. Последовательно останавливает загрузочные скрипты, расположенные в `/etc/rc.d/scripts/`;
2. Синхронизирует системные часы с часами компьютера;
3. Отключает все swap-разделы и/или swap-файлы;
4. Убивает все незавершённые процессы;
5. Размонтирует все подключенные файловые системы;

## Листинг

```bash
#!/bin/ash
# System shutdown script
# (C) 2024 mskrasnov <https://github.com/mskrasnov>

. /etc/rc.d/init.d/functions

echo -e "\nSystem is going down for reboot or halt now.\n"
echo -e "\n\e[1mStarting stop scripts.\e[0m"

export PATH=/bin:/sbin

for i in /etc/rc.d/scripts/*
do
  if [ -x $i ]; then
    $i stop
  fi
done

if [ -x /sbin/hwclock ] && [ -e /dev/rtc0 ]; then
  print_msg "Syncing system clock to hardware clock..."
  hwclock --systohc --utc
  check_status
fi

if [ -x /sbin/swapoff ] && [ -s /etc/fstab ]; then
  print_msg "Disabling swap space..."
  swapoff -a
  check_status
fi

print_msg "Syncing all filesystems..."
sync
check_status

echo "Killing all processes..."
kill -TERM -1
kill -KILL -1

echo "Unmounting all filesystems..."
umount -a -r

exit 0
```
