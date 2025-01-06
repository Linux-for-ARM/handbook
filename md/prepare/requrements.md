# Требования к хосту

## Оборудование

- Раздел на жёстком диске или просто свободное место, рекомендуемый объём которого - 10 Гб и более.
- Если оперативной памяти хост-компьютера мало (менее 4 Гб), рекомендуется создать раздел или файл подкачки. Кроме того, можно использовать `zram`.

## Программное обеспечение

Первое и самое важное - на компьютере должна быть установлена ОС Linux. Сборка на других системах семейства UNIX не проверялась и не рекомендуется.

Если у вас нет на компьютере установленной системы Linux, допускается сборка LFA в операционной системе Windows в окружении WSL. Выбор дистрибутива для запуска в WSL не имеет значения, главное здесь только наличие в дистрибутиве указанного ниже программного обеспечения. Однако сборка LFA в WSL не тестировалась и может не работать вовсе.

На вашей хост-системе или в окружении WSL должно быть установлено ПО из списка ниже с указанными минимальными версиями. Для большинства современных дистрибутивов Linux это не должно быть особой проблемой. Самое главное, чтобы версия, которую предоставляет используемый вами дистрибутив, не была ниже, чем в списке далее.

- `bash-3.2` (`/bin/sh` должна быть ссылкой на `bash`)
- `bc-1.07` (для компиляции Linux)
- `binutils-2.13`
- `bison-2.7` (`/usr/bin/yacc` должен быть ссылкой на `bison`)
- `coreutils-8.1`
- `diffutils-2.8.1`
- `findutils-4.2.31`
- `flex-2.6.4`
- `gawk-4.0.1` (`/usr/bin/awk` должен быть ссылкой на `gawk`)
- `gcc-5.2` (влючающий компилятор языка С, C++)
- `grep-2.5.1a`
- `gzip-1.3.12`
- `linux-4.19`
- `m4-1.4.10`
- `make-4.0`
- `ncurses-6.3` (для сборки BusyBox, Linux и U-Boot)
- `patch-2.5.4`
- `perl-5.8.8`
- `python-3.4`
- `rsync-3.2.7` (для установки заголовков ядра на этапе сборки кросс-компилятора)
- `sed-4.1.5`
- `setuptools-66.1` (для компиляции U-Boot)[^1]
- `swig-4.0` (для компиляции U-Boot)
- `tar-1.22`
- `texinfo-6.8` (для сборки binutils)
- `u-boot-tools-2023.01` (для сборки ядра Linux и работы с загрузчиком U-Boot)
- `xz-5.0`
- `wget-1.23` и `md5sum` (для скачивания исходного кода LFA)

```admonish warning title="Внимание"
Для некоторых моделей Allwinner SoC требуется сборка компонента `crust`, которая производится с помощью кросс-компилятора для архитектуры `or1k`. Здесь не приводится инструкций о его сборке, поскольку информация сразу о двух кросс-компиляторах (x86_64 -> ARM и x86_64 -> or1k) усложнит руководство и собьёт с толку тех читателей, кому or1k вовсе не нужен. Вы можете либо собрать нужный вам кросс-компилятор самостоятельно, либо использовать готовые пакеты: так, например, в репозиториях Arch Linux есть нужные пакеты с binutils и GCC для нужной архитектуры.
```

> Некоторые дистрибутивы включают в свои репозитории метапакет, объединяющий большинство описанных выше утилит. В зависимости от дистрибутива Linux название этого пакета может меняться. Например, в Debian этот пакет называется `build-essential`. Рекомендуем вам установить сначала его, а потом доустановить все недостающие пакеты.

## Проверка системных требований

Чтобы проверить наличие в вашей хост-системе всех необходимых версий необходимого ПО, выполните следующие команды:

```bash
cat > ver-check.sh << "EOF"
#!/bin/bash
# A script to list version numbers of critical development tools

# If you have tools installed in other directories, adjust PATH here

# For Linux for ARM (LFA) 2.0
# Forked from Linux from Scratch 12.2 (https://linuxfromscratch.org/lfs/view/stable-systemd/chapter02/hostreqs.html)

LC_ALL=C 
PATH=/usr/bin:/bin

bail() { echo -e "\e[1;31mFATAL:\e[0m $1"; exit 1; }
grep --version > /dev/null 2> /dev/null || bail "grep does not work"
sed '' /dev/null || bail "sed does not work"
sort   /dev/null || bail "sort does not work"

ver_check()
{
   if ! type -p $2 &>/dev/null
   then 
     echo "ERROR: Cannot find $2 ($1)"; return 1; 
   fi
   v=$($2 --version 2>&1 | grep -E -o '[0-9]+\.[0-9\.]+[a-z]*' | head -n1)
   if printf '%s\n' $3 $v | sort --version-sort --check &>/dev/null
   then 
     printf "OK:    %-9s %-6s >= $3\n" "$1" "$v"; return 0;
   else 
     printf "ERROR: %-9s ver. $v is TOO OLD ($3 or later required)\n" "$1"; 
     return 1; 
   fi
}

ver_check2() {
   if ! type -p $2 &>/dev/null
   then 
     echo "ERROR: Cannot find $2 ($1)"; return 1; 
   fi
   v=$($2 -version 2>&1 | grep -E -o '[0-9]+\.[0-9\.]+[a-z]*' | head -n1)
   if printf '%s\n' $3 $v | sort --version-sort --check &>/dev/null
   then 
     printf "OK:    %-15s %-6s >= $3\n" "$1" "$v"; return 0;
   else 
     printf "ERROR: %-15s ver. $v is TOO OLD ($3 or later required)\n" "$1"; 
     return 1; 
   fi
}

ver_kernel()
{
   kver=$(uname -r | grep -E -o '^[0-9\.]+')
   if printf '%s\n' $1 $kver | sort --version-sort --check &>/dev/null
   then 
     printf "OK:    Linux Kernel $kver >= $1\n"; return 0;
   else 
     printf "ERROR: Linux Kernel ($kver) is TOO OLD ($1 or later required)\n" "$kver"; 
     return 1; 
   fi
}

# Coreutils first because --version-sort needs Coreutils >= 7.0
ver_check  Coreutils      sort            8.1 || bail "Coreutils too old, stop"
ver_check  Bash           bash            3.2
ver_check  Bc             bc              1.07
ver_check  Binutils       ld              2.13
ver_check  Bison          bison           2.7
ver_check  Diffutils      diff            2.8.1
ver_check  Findutils      find            4.2.31
ver_check  Flex           flex            2.6.4
ver_check  Gawk           gawk            4.0.1
ver_check  GCC            gcc             5.2
ver_check  "GCC (C++)"    g++             5.2
ver_check  Grep           grep            2.5.1a
ver_check  Gzip           gzip            1.3.12
ver_check  M4             m4              1.4.10
ver_check  Make           make            4.0
ver_check  Ncurses        ncurses6-config 6.3
ver_check  Patch          patch           2.5.4
ver_check  Perl           perl            5.8.8
ver_check  Python         python3         3.4
ver_check  Rsync          rsync           3.2.7
ver_check  Sed            sed             4.1.5
ver_check2 Swig           swig            4.0
ver_check  Tar            tar             1.22
ver_check  Texinfo        texi2any        5.0
ver_check  "U-Boot Tools" mkimage         2023.01
ver_check  Xz             xz              5.0.0
ver_check2 Wget           wget            1.23
ver_kernel 4.19

if mount | grep -q 'devpts on /dev/pts' && [ -e /dev/ptmx ]
then echo "OK:    Linux Kernel supports UNIX 98 PTY";
else echo "ERROR: Linux Kernel does NOT support UNIX 98 PTY"; fi

alias_check() {
   if $1 --version 2>&1 | grep -qi $2
   then printf "OK:    %-4s is $2\n" "$1";
   else printf "ERROR: %-4s is NOT $2\n" "$1"; fi
}
echo "Aliases:"
alias_check awk GNU
alias_check yacc Bison
alias_check sh Bash

if [ "$(nproc)" = "" ]; then
   echo "ERROR: nproc is not available or it produces empty output"
else
   echo "OK: nproc reports $(nproc) logical cores are available"
fi
EOF

bash ver-check.sh
```

## Примеры для разных дистрибутивов

В разделе ниже представлены команды для установки необходимого для сборки ПО в основные дистрибутивы Linux. Еси вы не нашли свой дистрибутив здесь, обратитесь к его репозиториям с ПО и документации.

### Ubuntu/Debian

```bash
sudo apt install build-essential texinfo rsync u-boot-tools swig
```

---

[^1]: Это модуль языка Python, который может быть установлен с помощью пакетного менеджера `pip` (входит в состав Python и обычно устанавливается вместе с ним), либо с помощью пакетного менеджера вашего дистрибутива, если в его репозиториях поставляются пакеты для Python (в таком случае имя пакета, содержащего Python-модуль `setuptools`, может быть `python-setuptools` или `python3-setuptools`). Использование пакетного менеджера вашего дистрибутива вместо `pip` предпочтительнее, поскольку в таком случае `setuptools` будут установлены именно в систему, откуда интерпретатор Python будет иметь к нему доступ. С недавнего времени пакетный менеджер `pip` отключил «глобальную» установку Python-модулей в систему по умолчанию, став предпочитать установку модулей в виртуальное окружение Python.
