# Allwinner

Для плат, использующих SoC на базе Allwinner (`sunxi`), система сборки U-Boot генерирует единый интегрированный файл образа: `u-boot-sunxi-with-spl.bin`. Этот файл можно использовать на SD-картах, eMMC-устройствах, SPI-Flash и для метода загрузки с USB-OTG (FEL). Чтобы собрать этот файл, выполните следующие действия:

- Для 64-битных SoC сначала соберите Trusted Firmware (TF-A, ранее известный как ATF), для этого вам понадобится его файл `bl31.bin`. Более подробную информацию см. ниже.
- Опционально для 64-битных SoC следует собрать crost management processor firmware, для этого вам понадобится файл `scp.bin`. Подробнее см. ниже.
- Соберите U-Boot:

```bash
export BL31=/путь/до/bl31.bin
export SCP=/путь/до/scp.bin

make <имя платы>_defconfig
make
```

- Запишите его на карту памяти (micro)SD (подробнее см. ниже):

```bash
dd if=u-boot-sunxi-with-spl.bin of=/dev/sdX bs=8k seek=1
```

- Загружайтесь с этой карты.

```admonish warning title="Внимание"
Традиционное место на SD-карте, с которой загружается Allwinner BootROM - 8 КБ (сектор 16). Это хорошо работает со старой таблицей разделов MBR, с которой форматируется большинство SD-карт. Однако для таблицы разделов GPT это станет недействительным. Новые SoC (начиная с H3 с конца 2014 года) также поддерживают загрузку с 128 КБ, что выходит за рамки даже GPT и, следовательно, является более безопасным местом.
```

> Более подробную информацию, а также альтернативные места загрузки или установки см. ниже.

## Сборка ARM Trusted Firmware (TF-A)

Для плат, использующих 64-битный SoC (A64, H5, H6, H616, R329) требуется BL31 stage микропрограммы [Arm Trusted Firmware-A](https://www.trustedfirmware.org/projects/tf-a/). Это эталонная реализация безопасного программного обеспечения для ARMv8-A, предлагающая PSCI и SMCCC. Поддержка плат на базе Allwinner полностью реализована.

Для сборки файла `bl31.bin` введите:

```bash
git clone https://git.trustedfirmware.org/TF-A/trusted-firmware-a.git
cd trusted-firmware-a

make CROSS_COMPILE=$LFA_TGT- PLAT=sun50i_a64 DEBUG=1
export BL31=$PWD/build/sun50i_a64/debug/bl31.bin
```

> Целевая платформа (`PLAT=`) для SoC A64 и H5 - `sun50i_a64`, для H6 - `sun50i_h6`, для H616 - `sun50i_h616` и для R329 - `sun50i_r329`. Для поиска всех доступных платформ введите:
>
> ```bash
> find plat/allwinner -name platform.mk
> ```
>
> В файле [`docs/plat/allwinner.rst`](https://trustedfirmware-a.readthedocs.io/en/latest/plat/allwinner.html) содержится дополнительная информация и перечислены некоторые опции сборки.

## Сборка образа U-Boot

```admonish warning title="Внимание"
Предполагается, что у вас уже установлена переменная окружения `BL31`.
```

```bash
make <имя платы>_defconfig
make
```

Файл, содержащий всё необходимое, называется `u-boot-sunxi-with-spl.bin` и находится в корневой папке дерева исходного кода U-Boot. За исключением необработанных NAND-устройств его можно использовать для любого источника загрузки. Devicetree платы также включено.
