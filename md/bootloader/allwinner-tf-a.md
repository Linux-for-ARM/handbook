# Allwinner: Сборка TF-A

{{#include pkgs/tf-a.md}}

## Настройка

Вам нужно объявить переменную окружения `PLAT`, которая будет содержать имя целевой платформы для сборки:

```bash
export PLAT="целевая платформа"
```

> **Целевые платформы для сборки:**
>
> Сборка TF-A специфична для каждого SoC, в частности, специфично значение переменной `PLAT`, которая передаётся системе сборки `make`. Вы можете воспользоваться значениями из таблицы ниже:
>
> | SoC            | Платформа     |
> |----------------|---------------|
> | Allwinner A64  | `sun50i_a64`  |
> | Allwinner H5   | `sun50i_a64`  |
> | Allwinner H6   | `sun50i_h6`   |
> | Allwinner H616 | `sun50i_h616` |
> | Allwinner H313 | `sun50i_h616` |
> | Allwinner T507 | `sun50i_h616` |
> | Allwinner R329 | `sun50i_r329` |
>
> Для поиска всех целевых платформ введите:
>
> ```bash
> find plat/allwinner -name platform.mk
> ```
> В файле [`docs/plat/allwinner.rst`](https://trustedfirmware-a.readthedocs.io/en/latest/plat/allwinner.html) содержится дополнительная информация и приведены некоторые опции сборки.

Например, если в моей плате используется SoC Allwinner H6, то значение переменной `PLAT` будет равно `sun50i_h6`:

```bash
export PLAT="sun50i_h6"
```

## Сборка

```bash
make CROSS_COMPILE=$LFA_TGT- DEBUG=1
```

## Настройка окружения

Теперь вам нужно объявить переменную окружения `BL31`, содержащую путь до скомпилированной микропрограммы:

```bash
export BL31=$PWD/build/$PLAT/debug/bl31.bin
```

Необходимости в переменной `PLAT` больше нет, поэтому можете её удалить:

```bash
unset PLAT
```

```admonish warning title="Внимание"
Не удаляйте эту директорию с исходным кодом TF-A (в которой вы его собирали) до тех пор, пока не соберёте загрузчик U-Boot!
```

~~~admonish note title="Содержимое пакета" collapsible=true
- **Установленные файлы:** `$PWD/build/$PLAT/debug/bl31.bin`

### Описание компонентов

- `$PWD/build/$PLAT/debug/bl31.bin` — требуемый для сборки U-Boot компонент TF-A.
~~~
