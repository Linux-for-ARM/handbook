# Broadcom

<!--
ехал пенис через пенис
видит пенис — пенис пенис
пенис пенис через пенис
пенис пенис пенис пенис
-->

## Поддерживаемые платы

### SoC BCM7445 и BCM7260

Здесь U-Boot является загрузчиком третьего этапа, который запускается встроенным загрузчиком BOLT компании Broadcom.

BOLT загружает U-Boot как бинарный ELF-файл. Некоторые функции U-Boot, такие как работа с сетью, не реализованы, но есть некоторые другие важные функции, включая:

- Поддержка файловой системы `ext4`;
- Поддержка FIT-образов;
- Поддержка файлов devicetree из FIT-образа вместо таковых файлов из BOLT.

| SoC     | `defconfig` |
|---------|-------------|
| BCM7445 | `bcm7445`   |
| BCM7260 | `bcm7260`   |

### Raspberry Pi

| Плата                                | Архитектура    | `defconfig`    |
|--------------------------------------|----------------|----------------|
| **Raspberry Pi**                     | **32 бит**     | **`rpi`**      |
| Raspberry Pi 1/Raspberry Pi Zero     |                | `rpi_0_w`      |
| Raspberry Pi 2                       |                | `rpi_2`        |
| Raspberry Pi 3b                      |                | `rpi_3_32b`    |
| Raspberry Pi 4b                      |                | `rpi_4_32b`    |
| **Raspberry Pi 3b**                  | **64 бит**     | **`rpi_3`**    |
| Raspberry Pi 3b+                     |                | `rpi_3_b_plus` |
| Raspberry Pi 4b                      |                | `rpi_4`        |

Общая конфигурация:

| Плата                | `defconfig`     |
|----------------------|-----------------|
| Raspberry Pi 3b      | `rpi_arm64`[^1] |
| Raspberry Pi 3b+     |                 |
| Raspberry Pi 4b      |                 |
| Raspberry Pi 400     |                 |
| Raspberry Pi CM 3    |                 |
| Raspberry Pi CM 3+   |                 |
| Raspberry Pi CM 4    |                 |
| Raspberry Pi zero 2w |                 |

## Сборка

```bash
make CROSS_COMPILE=$LFA_TGT-
```

## Сохранение образа U-Boot

```bash
cp -v u-boot $LFA/bootloader.bin
```

[^1]: `rpi_arm64_defconfig` использует дерево устройств, предоставляемое прошивкой, вместо встроенного в U-Boot. Это позволяет использовать один и тот же бинарник U-Boot для загрузки с разных плат.
