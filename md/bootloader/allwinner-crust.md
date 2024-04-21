# Allwinner: Сборка SCP (crust)

{{#include pkgs/crust.md}}

```admonish warning title="Внимание"
Сборка пакета осуществляется с помощью кросс-компилятора `or1k-none-elf`.
```

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
