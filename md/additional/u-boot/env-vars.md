# Переменные окружения

Загрузчик U-Boot поддерживает пользовательскую конфигурацию с помощью переменных окружения, значения которых можно записать на постоянном носителе (например, во flash-памяти).

Переменные окружения устанавливаются с помощью команды `env set` (алиас `setenv`), выводятся в консоль с помощью команды `env print` (алиас `printenv`) и сохраняются в постоянном хранилище с помощью команды `env save` (`saveenv`). Использование `env set` без указания значения переменной может использоваться для удаления переменной из окружения. Пока вы не сохраняете окружение, вы работаете с его копией в оперативной памяти. Если область в постоянном хранилище, содержащая окружение, будет случайно стёрта, U-Boot создаст окружение по умолчанию.

Некоторые настройки контролируются переменными окружения, поэтому установка переменной может изменить поведение загрузчика (например, таймаут автозагрузки, автозагрузка с `tftp` и т.п.).

## Окружение в текстовых файлах

Для каждой конкретной платы компьютера может быть создано своё уникальное окружение, переменные которого хранятся в файле `*.env`, имеющий простой текстовый формат. Базовое имя этого файла содержится в параметре `CONFIG_ENV_SOURCE_FILE` или, если он пуст, в `CONFIG_SYS_BOARD`.

Этот файл хранится в каталоге, отведённом для конкретной платы, и имеет расширение `.env`. Пример пути до этого файла:

```
board/<производитель>/<плата>/<CONFIG_ENV_SOURCE_FILE>.env
```

или:

```
board/<производитель>/<плата>/<CONFIG_SYS_BOARD>.env
```

Это обычный текстовый файл, в котором хранятся переменные в формате `var=value`. Поддерживаются пустые строки и многострочные переменные. Пробелы перед `=` не допускаются.

Для добавления дополнительного текста к значению переменной можно использовать конструкцию `var+=value`. Этот текст объединится со значением переменной во время сборки и станет доступным загрузчику как единое значение. Переменные могут содержать символ `+`, но если вам вдруг захочется иметь значение переменной, заканчивающееся на этот символ, то поставьте перед `+` обратную косую черту, чтобы скрипт загрузчика знал, что вы не добавляете значение к существующей переменной, а объявляете новую:

```
maximum\+=value
```

Этот файл может включать комментарии в стиле C. Пустые линии и многострочные переменные также поддерживаются, кроме того, вы можете использовать привычные директивы препроцессора C и определения `CONFIG` из конфига вашей платы.

Например, для платы `snapper9260` вы можете создать текстовый файл с именем `board/bluewater/snapper9260.env`, содержащий информацию об окружении:

```c
stdout=serial
#ifdef CONFIG_VIDEO
stdout+=,vidconsole
#endif
bootcmd=
    /* U-Boot script for booting */

    if [ -z ${tftpserverip} ]; then
        echo "Use 'setenv tftpserverip a.b.c.d' to set IP address."
    fi

    usb start; setenv autoload n; bootp;
    tftpboot ${tftpserverip}:
    bootm
failed=
    /* Print a message when boot fails */
    echo CONFIG_SYS_BOARD boot failed - please check your image
    echo Load address is CONFIG_SYS_LOAD_ADDR
```

Настройки, которые являются общими для нескольких плат, можно подключать к `.env`-файлу конкретной платы с помощью директивы `#include`, которой будет передан файл, находящийся в директории `include/env`, содержащий настройки окружения. Например:

```c
#include <env/ti/mmc.env>
```

## Старый C-стиль окружения

Если параметр `CONFIG_ENV_SOURCE_FILE` пуст и имя `.env`-файла по умолчанию отсутствует, то вместо него используется окружение в старом C-стиле (см. ниже).

Традиционно, стандартное окружение создаётся в файле `include/env_default.h`. Оно может быть дополнено различными определениями `CONFIG`. В частности, вы можете определить `CFG_EXTRA_ENV_SETTINGS` в конфиге конкретной платы, чтобы добавить переменные окружения.

## Список переменных окружения

Некоторые параметры конфигурации загрузчика можно задать с помощью переменных окружения. Во многих случаях значения в окружении по умолчанию берётся из опции `CONFIG` — для этого см. `include/env_default.h`.

Неполный список переменных (более полный список см. в [**документации U-Boot**](https://docs.u-boot.org/en/latest/usage/environment.html#list-of-environment-variables)):

> **`autostart`**
>
> Если установлено значение `yes` (фактически любая строка, начинающаяся с `1`, `y`, `Y`, `t` или `T`), образ, загруженный с помощью одной из перечисленных ниже команд, будет запущен автоматически внутренним вызовом команды `bootm`.
>
> - `bootelf` — загрузка из ELF-файла, загруженного в оперативную память;
> - `bootp` — загрузка образа по сети используя протокол BOOTP/TFTP;
> - `dhcp` — загрузка образа по сети используя протокол DHCP/TFTP;
> - `diskboot` — загрузка с IDE-устройства;
> - `nboot` — загрузка с NAND-устройства;
> - `nfs` — загрузка образа по сети используя протокол NFS;
> - `rarpboot` — загрузка образа по сети используя протокол RARP/TFTP;
> - `scsiboot` — загрузка с SCSI-устройства;
> - `tftpboot` — загрузка образа по сети используя TFTP-протокол;
> - `usbboot` — загрузка с устройства USB;
>
> Если переменная окружения `autostart` не имеет значения, начинающегося с `1`, `y`, `Y`, `t` или `T`, образ, переданный команде `bootm`, будет скопирован по адресу загрузки (и в конечном итоге распакован), но **не будет** запущен. Это можно использовать для загрузки и распаковки произвольных данных.

> **`baudrate`**
>
> Используется для установки скорости передачи данных по UART — значение по умолчанию указано в параметре `CONFIG_BAUDRATE` (по умолчанию равна 115200).

> **`bootdelay`**
>
> Задержка перед автоматическим запуском `bootcmd`. В течение этого времени пользователь может выбрать вход в оболочку или меню загрузки U-Boot (если `CONFIG_AUTOBOOT_MENU_SHOW=y`):
>
> - 0 — автозагрузка без задержки, но её можно остановить вводом клавиши;
> - 1 — отключение автозагрузки;
> - 2 — автозагрузка без задержки и без проверки на прерывание.
>
> Значение по умолчанию определяется параметром `CONFIG_BOOTDELAY`. Значение `bootdelay` переопределяется значением `/config/bootdelay` в Device Tree, если `CONFIG_OF_CONTROL=y`.

> **`bootcmd`**
>
> Команда, которая выполняется, если пользователь не вошёл в оболочку U-Boot во время задержки загрузки.

> **`bootargs`**
>
> Аргументы командной строки, которые будут переданы во время загрузки операционной системе или двоичному образу.

> **`fdt_high`**
>
> Если установлено, этот параметр ограничит максимальный адрес, в который будет скопирован образ FDT (Flattened Device Tree) при загрузке. Например, если у вас система с 1 Гб памяти по физическому адресу 0x10000000, а ядро Linux распознаёт только первые 704 МБ как low memory, вам может понадобиться установить `fdt_high=0x3C000000`, чтобы FDT был скопирован по максимальному адресу low memory 704 МБ, чтобы ядро Linux могло получить к нему доступ во время процесса загрузки.
>
> Если этот параметр имеет специальное значение `0xffffffffff` (32-битные устройства) или `0xffffffffffffff` (64-битные устройства), то FDT вообще не будет копироваться при загрузке.

> **`initrd_high`**
>
> Ограничивает позиционирование образа `initrd`. Если эта переменная не установлена, образы `initrd` будут копироваться по максимально возможному адресу в оперативной памяти; обычно это то, что нужно, поскольку позволяет обеспечить максимальный размер образа `initrd`. Однако если по какой-то причине вы хотите быть уверены, что образ `initrd` будет загружен ниже предела `CFG_SYS_BOOTMAPSZ`, вы можете установить для этой переменной значение `no`, `off` или `0`. В качестве альтернативы можно задать максимальный верхний адрес для использования (U-Boot всё равно будет проверять, не перезаписывает ли этот образ стек и данные загрузчика).
>
> Например, вы имеете систему с 16 МБ ОЗУ и хотите зарезервировать 4 МБ для использования Linux, вы можете это сделать, добавив `mem=12M` к значению переменной `bootargs`. Однако теперь вы должны будете убедиться, что образ `initrd` будет размещён в первых 12 МБ — это можно сделать с помощью:
>
> ```bash
> setenv initrd_high 00c00000
> ```
>
> Если этот параметр использует специальное значение `0xffffffffff` (32-битные устройства) или `0xffffffffffffff` (64-битные устройства), это будет означать для загрузчика, что все адреса являются легальными для ядра Linux, включая адреса во флеш-памяти. В этом случае U-Boot вообще не будет копировать ramdisk. Это может быть полезно для уменьшения времени загрузки системы, но требует, чтобы эта функция поддерживалась ядром Linux. Кроме того, нужно, чтобы пользователь убедился в отсутствии дублирования с другими частями образа, такими как BSS ядра Linux. Этот параметр не следует включать по умолчанию, а только в рамках оптимизации развёртывания ОС.

> **`loadaddr`**
>
> Устанавливает стандартный адрес загрузки для таких команд, как `bootp`, `rarpboot`, `tftpboot`, `loadb` или `diskboot`. Обратите внимание, что оптимальные значения по умолчанию в разных архитектурах могут различаться. Например, на 32-битных ARM используется некоторое смещение от начала памяти, так как в ядре Linux zImage имеет самораспаковывающийся декомпрессор, и лучше, если мы не будем вмешиваться в работу этого декомпрессора.

> **`silent_linux`**
>
> Если эта переменная установлена, то Linux будет загружаться в «тихом режиме».

## Расположения образов

Следующие переменные содержат расположение образов, используемых при загрузке. Столбец «Образ» указывает роль образа и не является именем переменной окружения. Остальные столбцы — имена переменных. «Имя файла» — имя файла на TFTP-сервере. «Адрес ОЗУ» — место в ОЗУ, куда будет загружен образ, а «Расположение Flash» — адрес образа во flash-памяти NOR или смещение во flash-памяти NAND.

```admonish warning title="Важно"
Эти переменные не обязательно должны быть определены для всех плат, некоторые платы в настоящее время используют другие переменные для этих целей, а некоторые используют эти переменные для других целей.
```

Также обратите внимание, что большинство из этих переменных — это просто общепринятый набор имён переменных, используемых в некоторых других определениях переменных, но не закодированных в коде загрузчика.

| Образ           | Имя файла     | Адрес ОЗУ        | Расположение Flash |
|-----------------|---------------|------------------|--------------------|
| Ядро Linux      | `bootfile`    | `kernel_addr_r`  | `kernel_addr`      |
| Блоб Devicetree | `fdtfile`     | `fdt_addr_r`     | `fdt_addr`         |
| ramdisk         | `ramdiskfile` | `ramdisk_addr_r` | `ramdisk_addr`     |

При задании адресов ОЗУ для `kernel_addr_r`, `fdt_addr_r` и `ramdisk_addr_r` необходимо учитывать несколько типов ограничений. Одним из таких типов является требование к полезной нагрузке. Например, devicetree **ДОЛЖНО** загружаться по адресу, выровненному по 8 байтам, так как этого требует спецификация. Аналогичным образом операционная система может определять ограничения на то, где в памяти может находиться полезная нагрузка. Это документировано, например, в Linux, в документах [**Booting ARM Linux**](https://www.kernel.org/doc/html/latest/arm/booting.html) и [**Booting AArch64 Linux**](https://www.kernel.org/doc/html/latest/arm64/booting.html). Наконец, существуют практические ограничения. Мы не знаем, какой размер конкретной полезной нагрузки будет задействовать пользователь, но каждая полезная нагрузка не должна перекрываться, иначе она будет повреждать другую полезную нагрузку. Аналогичная проблема может возникнуть, если полезная нагрузка окажется в области OS BSS. По этим причинам нам нужно убедиться, что значения по умолчанию здесь не приведут к сбоям в загрузке и достаточно объяснимы, чтобы их можно было оптимизировать по времени загрузки или скорректировать для конфигураций с меньшим объемом памяти.

На разных архитектурах у нас будут разные ограничения. Выжно следовать всем документированным требованиям, чтобы наилучшим образом обеспечить совместимость. В [**документации U-Boot**](https://docs.u-boot.org/en/latest/usage/environment.html#texas-instruments-omap2plus-armv7-example) приведены примеры, показывающие, как обеспечить разумные значения по умолчанию в различных случаях.