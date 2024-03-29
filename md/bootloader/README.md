# Сборка загрузчика

{{#include pkgs/u-boot.md}}

## Примерный порядок сборки

Для некоторых плат перед сборкой U-Boot необходимо собрать предварительные файлы. Например, для некоторых плат необходимо собрать ARM Trusted Firmware. Для получения более подробных сведений смотрите окументацию к поддерживаемых в LFA платах далее.

После чего требуется собрать U-Boot и записать полученный образ на карту памяти.

## Настройка

Директория `configs/` содержит шаблоны конфигурационных файлов для поддерживаемых [проектом U-Boot, а не LFA] плат в соответствии со следующей схемой наименования:

```
<имя платы>_defconfig
```

Эти файлы лишены настроек по умолчанию. Поэтому вы не можете использовать их напрямую. Вместо этого их имя служит в качестве цели `make` для генерации фактического конфигурационного файла `.config`. Например, шаблон конфигурации для платы Odroid C2 называется `odroid-c2_defconfig`. Соответствующий файл `.config` генерируется командой:

```bash
make odroid-c2_defconfig
```

> **Для плат на базе SoC Allwinner:**
>
> На вики [linux-sunxi](https://linux-sunxi.org/) также можно найти имя `defconfig` файла на соответствующей странице платы.

Вы можете сконфигурировать пакет командой:

```bash
make menuconfig
```

## Сборка

> Для сборки вам по прежгнему нужен наш кросс-компилятор.

```bash
CROSS_COMPILE=$LFA_TGT- make
```

### Компилятор Devicetree

Платам, использующим `CONFIG_OF_CONTROL` (т.е. почти всем), нужен компилятор [Devicetree](../additional/dtb.md) (`dtc`). Платам с `CONFIG_PYLIBFDT` требуется `pylibfdt` (библиотека Python для доступа к данным Devicetree). Подходящие версии этих библиотек включены в дерево U-Boot в директории `scripts/dtc` и собираются автоматически по мере необходимости.

Если вы хотите использовать их системные версии, используйте переменную `DTC`, в которой будет указан путь до `dtc`:

```bash
CROSS_COMPILE=$LFA_TGT- DTC=/usr/bin/dtc make
```

В этом случае `dtc` и `pylibfdt` не будут собраны. Система сборки проверит, что версия `dtc` достаточно новая. Она также убедится, что `pylibfdt` присутствует, если это необходимо.

Обратите внимание, что инструменты [Host Tools](https://docs.u-boot.org/en/latest/build/tools.html) всегда собираются с включенной версией `libfdt`, поэтому в настоящее время невозможно собрать U-Boot с системной `libfdt`.

### LTO

U-Boot поддерживает link-time optimisation, которая может уменьшить размер скомпилированных двоичных файлов, особенно при использовании SPL.

В настоящее время эта функция может быть включена на платах ARM путём добавления `CONFIG_LTO=y` в файл `defconfig`.

Однако в таком случае загрузчик будет собираться несколько медленнее, чем без LTO.

## Установка

Процесс установки U-Boot специфичен для каждого компьютера. На данный момент в руководстве поддерживаются компьютеры на базе SoC [Allwinner](allwinner.md), [Broadcom](broadcom.md) и [Rockchip](rockchip.md), а также установка U-Boot для эмуляции в [QEMU](qemu.md).
