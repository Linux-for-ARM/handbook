# Allwinner: Сборка SCP (crust)

{{#include pkgs/crust.md}}

```admonish warning title="Внимание"
Сборка пакета осуществляется с помощью кросс-компилятора `or1k-none-elf`.
```

> **Патчи:** для `crust` вы можете найти дополнительные опциональные патчи в [**репозитории Armbian**](https://github.com/armbian/build/tree/main/patch/u-boot/u-boot-sunxi-crust).

> Если вы собираете систему для OrangePi 3 LTS, можете применить патч [`add-defconfig-for-orangepi-3-lts`](https://github.com/armbian/build/blob/main/patch/crust/add-defconfig-for-orangepi-3-lts.patch). Если вы собираете систему для другого компьютера, оснащённого SoC H3, H5, H6, A64, можете применить [**соответствующий патч**](https://github.com/armbian/build/blob/main/patch/crust/add-defconfig-for-h3-h5-h6-a64-platforms.patch) для добавления их поддержки.

## Настройка

```bash
make <имя платы>_defconfig
```

> Список поддерживаемых материнских плат смотрите в директории [`configs/`](https://github.com/crust-firmware/crust/tree/master/configs). Например, для Orange Pi 3 замените `<имя платы>` на `orangepi_3`. Прочитайте также [**README**](https://github.com/crust-firmware/crust/blob/master/README.md#building-the-firmware)-файл из репозитория crust для получения дополнительных сведений о процессе сборки этой микропрограммы.

## Сборка

```bash
make CROSS_COMPILE=or1k-none-elf- scp
```

## Установка

Вам не нужно никуда копировать собранные программы, просто объявите новую переменную окружения `SCP`:

```bash
export SCP=$PWD/build/scp/scp.bin
```

```admonish warning title="Внимание"
Не удаляйте эту директорию с исходным кодом crust (в которой вы его собирали) до тех пор, пока не соберёте загрузчик U-Boot!
```

~~~admonish note title="Содержимое пакета" collapsible=true
- **Установленные файлы:** `$PWD/build/scp/scp.bin`

### Описание компонентов

- `$PWD/build/scp/scp.bin` — требуемый для сборки U-Boot компонент crust, предназначенный для управления питанием.
~~~
