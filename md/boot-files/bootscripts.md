# Загрузочные скрипты

{{#include pkgs/bootscripts.md}}

## inittab

Для начала создайте файл `/etc/inittab`, отвечающий за такие вещи как зарузка системы, её выключение и обработки поведения при нажатии комбинации <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Del</kbd>.

```bash
cat >> $LFA_SYS/etc/inittab << "EOF"
# Begin /etc/inittab

::sysinit:/etc/rc.d/startup

tty1::respawn:/sbin/getty 38400 tty1
tty2::respawn:/sbin/getty 38400 tty2
tty3::respawn:/sbin/getty 38400 tty3
tty4::respawn:/sbin/getty 38400 tty4
tty5::respawn:/sbin/getty 38400 tty5
tty6::respawn:/sbin/getty 38400 tty6

::shutdown:/etc/rc.d/shutdown
::ctrlaltdel:/sbin/reboot

# End /etc/inittab
EOF
```

## Скрипты

```bash
make DESTDIR=$LFA_SYS
```

---

> **Смотрите также:**
>
> - [Заметки об ОС Linux. Часть 3. Система инициализации](../additional/os-structure3.md);
> - [**SysV init must die**](https://busybox.net/~vda/init_vs_runsv.html) (<https://busybox.net/>).
