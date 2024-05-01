# Rockchip: Сборка U-Boot

{{#include pkgs/u-boot.md}}

```admonish warning title="Внимание"
Предполагается, что у вас уже установлены нужные переменные окружения, в частности `BL31` и, опционально, `ROCKCHIP_TPL`.
```

## Настройка

Объявите переменную окружения `TARGET`, которая будет содержать название SoC, для которого производится сборка загрузчика.

```bash
export TARGET="целевая платформа"
```

> **Целевые платформы загрузчика:**
>
> | SoC    | `defconfig`  |
> |--------|--------------|
> | px30   | `evb-px30`   |
> | rk3066 | `mk808`      |
> | rk3288 | `evb-rk3288` |
> | rk3308 | `evb-rk3308` |
> | rk3328 | `evb-rk3328` |
> | rk3368 | `evb-px5`    |
> | rk3399 | `evb-rk3399` |
> | rk3568 | `evb-rk3568` |
> | rk3588 | `evb-rk3588` |

Например, если в моей плате используется Rockchip RK3588, то значение переменной `TARGET` будет равно `evb-rk3588`:

```bash
export TARGET="evb-rk3588"
```

Создайте базовый конфиг для сборки U-Boot (`defconfig`):

```bash
make ${TARGET}_defconfig
```

## Сборка

```bash
make CROSS_COMPILE=$LFA_TGT-
```

## Сохранение образа U-Boot

Скопируйте скомпилированный файл в директорию `$LFA` для удобного доступа к нему в будущем:

```bash
cp -v u-boot-rockchip.bin $LFA/bootloader.bin
```

{{#include u-boot-save.md}}

~~~admonish note title="Содержимое пакета" collapsible=true
- **Установленные файлы:** `$LFA/bootloader.bin`

### Описание компонентов

- `$LFA/bootloader.bin` — скомпилированный файл загрузчика U-Boot.
~~~
