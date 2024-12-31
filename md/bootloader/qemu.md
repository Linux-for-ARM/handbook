# Эмуляция в QEMU (ARM)

{{#include pkgs/u-boot.md}}

## Настройка U-Boot

Установите имя аргумента `qemu_*_defconfig` в зависимости от архитектуры, для которой вы собираете:

```bash
if [ $LFA_TGT == "aarch64-linux-musleabihf" ]
then
  QEMU_ARCH="arm64"
else
  QEMU_ARCH="arm"
fi
```

Сконфигурируйте пакет U-Boot:

```bash
make CROSS_COMPILE=$LFA_TGT- \
  qemu_${QEMU_ARCH}_defconfig
```

### ACPI в QEMU

QEMU (начиная с версии v8.0.0) может предоставлять таблицы ACPI для ARM[^1]. Для их поддержки нужны следующие настройки U-Boot:

```bash
CONFIG_CMD_QFW=y
CONFIG_ACPI=y
CONFIG_GENERATE_ACPI_TABLE=y
```

Вместо того, чтобы обновлять файл `.config` вручную, вы можете добавить опцию `acpi.config` в команду `make`. Например:

```bash
make CROSS_COMPILE=$LFA_TGT-  \
  qemu_${QEMU_ARCH}_defconfig \
  acpi.config
```

## Сборка

```bash
make CROSS_COMPILE=$LFA_TGT-
```

В итоге будет сгенерирован двоичный файл `u-boot.bin`.

```admonish warning title="Важно"
В разделах о сборке загрузчика U-Boot для SoC Allwinner, Broadcom и Rockchip предполагается, что собранный двоичный файл с загрузчиком будет «встроен» в `img`-образ, который будет сгенерирован в разделе №8 «Сборка образа». Здесь же таких действий совершать не требуется — всё, что вам нужно, так это скопировать собранный двоичный файл загрузчика в специально отведённое для этого место, **не встраивая** его в генерируемый образ системы.
```

## Сохранение образа U-Boot

Скопируйте скомпилированный файл в директорию `$LFA` для удобного доступа к нему в будущем:

```bash
cp -v u-boot.bin $LFA/bootloader.bin
```

Также вместо `u-boot.bin` вы можете использовать образ `u-boot-nodtb.bin`, если не хотите использовать скомпилированные файлы Devicetree.

---

> **Смотрите также:**
>
> - [**QEMU ARM — Das U-Boot**](https://docs.u-boot.org/en/latest/board/emulation/qemu-arm.html) (<https://docs.u-boot.org/en/latest/>).

[^1]: На x86 эти настройки уже включены по умолчанию. Для ARM и RISC-V по умолчанию используются device-tree.
