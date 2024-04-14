# /etc/rc.d/startup

`/sbin/init` выполняет этот скрипт для запуска системных компонентов и служб.

## Что делает скрипт

1. Монтирует файловые системы `/proc`, `/sys`, `/tmp`, `/dev`;
2. Монтирует в `tmpfs` все директории, файлы в которых очень часто изменяются (например, логи). Это нужно для того, чтобы продлить жизнь ненадёжным SD- и eMMC-накопителям, на которых обычно будет запускаться система LFA;
3. Запускает `mdev`;
4. Настраивает системные часы;
5. Включает подкачку (swap), если она есть;
6. Настраивает сетевой интерфейс `lo`;
7. Последовательно запускает загрузочные скрипты из директории `/etc/rc.d/scripts/`.

## Листинг

```bash
#!/bin/ash
# System startup script
# (C) 2024 mskrasnov <https://github.com/mskrasnov>

. /etc/rc.d/init.d/functions

export PATH=/bin:/sbin

function mount_to_tmpfs() {
  mount -t tmpfs none -o nodev,nosuid,noatime /var/log &&
  mount -t tmpfs none -o nodev,nosuid,noatime /var/run &&
  mount -t tmpfs none -o nodev,nosuid,noatime /run
}

echo "Mounting kernel virtual file systems..."
mount -vt proc  none /proc
mount -vt sysfs none /sys
mount -vt tmpfs /tmp /tmp

mkdir -pv /dev/pts
mkdir -pv /dev/shm

echo "/sbin/mdev" > /proc/sys/kernel/hotplug

print_msg "Starting mdev..."
mdev -s
check_status

print_msg "Mounting /dev/pts..."
mount -t devpts none /dev/pts
check_status

print_msg "Mounting shared memory..."
mount -t tmpfs none /dev/shm
check_status

print_msg "Mounting temporary, log and variable dirs..."
mount_to_tmpfs
check_status

if [ -x /sbin/hwclock ] && [ -e /dev/rtc0 ]; then
  print_msg "Setting system clock..."
  hwclock --hctosys --utc
  check_status
fi

if [ -x /sbin/swapon ]; then
  print_msg "Enabling swap..."
  swapon -a
  check_status
fi

print_msg "Setting up interface [lo]..."
ifconfig lo up 127.0.0.1
check_status

echo -e "\n\e[1mRunning bootscripts\e[0m"

for i in /etc/rc.d/scripts/*
do
  if [ -x $i ]; then
    $i start
  fi
done

exit 0
```
