# Загрузочные скрипты

```admonish warning title="Внимание"
Это заготовка страницы. Здесь приведены общие инструкции, тестирование которых не производилось. Окончательная версия страницы войдёт во вторую версию руководства LFA.
```

## inittab

Для начала создайте файл `/etc/inittab`, отвечающий за такие вещи как зарузка системы, её выключение и обработки поведения при нажатии комбинации <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Del</kbd>.

```bash
cat >> $LFA_SYS/etc/inittab << "EOF"
::sysinit:/etc/rc.d/rc.S
::respawn:-/bin/sh -l
::ctrlaltdel:/sbin/reboot 
::shutdown:/etc/rc.d/rc.0
EOF
```

## Скрипты

Создайте директорию со скриптами:

```bash
mkdir -pv $LFA_SYS/etc/rc.d
```

Скрипт `$LFA_SYS/etc/rc.d/rc.0` размонтирует диски при выключении системы:

```bash
cat > $LFA_SYS/etc/rc.d/rc.0 << "EOF"
#!/bin/ash

sync
/sbin/umount -a -r > /dev/null 2>&1
EOF
```

Скрипт `$LFA_SYS/etc/rc.d/rc.S` выполняется при загрузке:

```bash
cat > $LFA_SYS/etc/rc.d/rc.S << "EOF"
#!/bin/ash

export PATH=/bin:/sbin

mount -v proc /proc -t proc

mkdir -pv /dev/pts
mount -vt devpts -o noexec,nosuid,gid=5,mode=0620 devpts /dev/pts

# Временные файлы лучше держать в ОЗУ, чтобы снизить число операций
# чтения/записи на SD/eMMC накопителе
mount -vt tmpfs none -o nodev,nosuid,noatime /tmp
mount -vt tmpfs none -o nodev,nosuid,noatime /var/log
mount -vt tmpfs none -o nodev,nosuid,noatime /var/run
mount -vt tmpfs none -o nodev,nosuid,noatime /run

mount -v sysfs /sys -t sysfs

# Запускаем системный логгер и логгер ядра
syslogd
sleep 1
klogd -c 3

echo "Press <Enter>..."
EOF
```

---

> **Смотрите также:**
>
> - [Заметки об ОС Linux. Часть 3. Система инициализации](../additional/os-structure3.md);
> - [**SysV init must die**](https://busybox.net/~vda/init_vs_runsv.html) (<https://busybox.net/>).
