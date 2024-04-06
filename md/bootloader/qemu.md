# Эмуляция в QEMU (ARM)

## ACPI в QEMU

QEMU (начиная с версии v8.0.0) может предоставлять таблицы ACPI для ARM. Для их поддержки нужны следующие настройки U-Boot:

```bash
CONFIG_CMD_QFW=y
CONFIG_ACPI=y
CONFIG_GENERATE_ACPI_TABLE=y
```

Вместо того, чтобы обновлять файл `.config` вручную, вы можете добавить опцию `acpi.config` в команду `make`. Например:

```bash
make orangepi-3_defconfig acpi.config
```

## Эмуляция блочных устройств

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

## Настройка U-Boot

Установите имя аргумента `qemu_*_defconfig` в зависимости от архитектуры, для которой вы собираете:

```bash
if [ $LFA_TGT -eq "aarch64-linux-musleabihf" ]
then
  QEMU_DEFCONFIG_ARCH="arm64"
else
  QEMU_DEFCONFIG_ARCH="arm"
fi
```

Сконфигурируйте пакет U-Boot:

```bash
make CROSS_COMPILE=$LFA_TGT- \
  qemu_${QEMU_DEFCONFIG_ARCH}_defconfig
```

## Сборка

```bash
make
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

---

> **Смотрите также:**
>
> - [QEMU ARM — Das U-Boot](https://docs.u-boot.org/en/latest/board/emulation/qemu-arm.html) (документация U-Boot).
