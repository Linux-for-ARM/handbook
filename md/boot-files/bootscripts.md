# Загрузочные скрипты

{{#include pkgs/bootscripts.md}}

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

```bash
make DESTDIR=$LFA_SYS
```

---

> **Смотрите также:**
>
> - [Заметки об ОС Linux. Часть 3. Система инициализации](../additional/os-structure3.md);
> - [**SysV init must die**](https://busybox.net/~vda/init_vs_runsv.html) (<https://busybox.net/>).
