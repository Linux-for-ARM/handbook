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
make qemu_${QEMU_ARCH}_defconfig acpi.config
```

## Сборка

```bash
make CROSS_COMPILE=$LFA_TGT-
```

## Запуск U-Boot

Минимальная команда для запуска эмулятора QEMU с загрузчиком U-Boot выглядит так:

- для AArch64:

```bash
qemu-system-aarch64 -machine virt \
  -nographic \
  -cpu cortex-a57 \
  -bios u-boot.bin
```

- для других архитектур семейства ARM:

```bash
qemu-system-arm -machine virt \
  -nographic \
  -bios u-boot.bin
```

> **Объяснение новых значений:**
>
> `-nographic` — обеспечивает вывод данных в терминал;
>
> `-cpu cortex-a57` — по какой-то странной причине программе `qemu-system-aarch64` необходимо явно указать использование 64-битного процессора, иначе эмулятор запустится в 32-битном режиме.

Вы также можете создать образ, в котором будут храниться сохранённые переменные окружения U-Boot. Это можно сделать, выполнив следующие действия:

- Создать образ `envstore.img` с помощью `qemu-img`:

```bash
qemu-img create -f raw envstore.img 64M
```

- Передать команде для запуска виртуальной машины параметр `pflash drive`:

```bash
  -drive if=pflash,format=raw,index=1,file=envstore.img
``` 

## Эмуляция блочных устройств

Поскольку командой выше вы только запустили загрузчик. Однако помимо загрузчика нужно передать аргументы, указывающие на образ операционной системы (генерацию такого образа см. далее в руководстве).

QEMU может эмулировать обычные блочные устройства. Добавьте следующие параметры в команду `qemu-system-aarch64` (или `qemu-system-arm`):

- MMC:

```bash
  -device sdhci-pci,sd-spec-version=3 \
  -drive if=none,file=disk.img,format=raw,id=MMC1 \
  -device sd-card,drive=MMC1
```

- NVMe:

```bash
  -drive if=none,file=disk.img,format=raw,id=NVME1 \
  -device nvme,drive=NVME1,serial=nvme-1
```

- SATA:

```bash
  -device ahci,id=ahci0 \
  -drive if=none,file=disk.img,format=raw,id=SATA1 \
  -device ide-hd,bus=ahci0.0,drive=SATA1
```

- USB:

```bash
  -device qemu-xhci \
  -drive if=none,file=disk.img,format=raw,id=USB1 \
  -device usb-storage,drive=USB1
```

> Во всех вариантах аргументов командной строки из этого пункта замените имя `disk.img` на название сгенерированного образа с системой. Подробнее о сборке образа с системой см. в пункте №8 [«Сборка образа»](../create-img.md).

## Дополнительные устройства

Возможно, для работы вашей системы понадобится эмуляция дополнительных устройств. Ниже представлены аргументы для команды запуска виртуальной машины QEMU, включающие эмуляцию некоторых из них.

- Чтобы добавить видеоконтроллер, удалите аргумент `-nographic`, заменив его, например, следующим:

```bash
  -serial stdio -device VGA
```

- Для добавления генератора псевдослучайных чисел, добавьте аргумент:

```bash
  -device virtio-rng-pci
```

## Ещё немного про виртуализацию

QEMU для ARM поддерживает специальную виртуальную машину `virt`, предоставляющую следующие базовые функции:

- Свободно настраиваемое количество ядер процессора;
- U-Boot, который загружается и выполняется по адресу `0x0`;
- Сгенерированный блоб дерева устройств, помещённый в начало оперативной памяти;
- Свободно конфигурируемый объём ОЗУ, описываемый в `*.dtb`;
- Последовательный порт PL011, обнаруживаемый в `*.dtb`;
- Таймер (для архитектуры ARMv7/ARMv8);
- PSCI для перезагрузки системы;
- Общий хост-контроллер PCI на базе ECAM, обнаруживаемый в `*.dtb`;

Кроме того, к PCI шине можно подключить ряд дополнительных периферийных устройств.

См. раздел [**Devicetree in QEMU**](https://docs.u-boot.org/en/latest/develop/devicetree/dt_qemu.html) в документации U-Boot для получения информации о том, как увидеть дерево устройств, фактически сгенерированное QEMU.

---

> **Смотрите также:**
>
> - [**QEMU ARM — Das U-Boot**](https://docs.u-boot.org/en/latest/board/emulation/qemu-arm.html) (<https://docs.u-boot.org/en/latest/>).

[^1]: На x86 эти настройки уже включены по умолчанию. Для ARM и RISC-V по умолчанию используются device-tree.
