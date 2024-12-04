# Allwinner: Сборка U-Boot

{{#include pkgs/u-boot.md}}

```admonish warning title="Внимание"
Предполагается, что у вас уже установлены нужные переменные окружения, в частности `BL31` и, опционально, `SCP`.
```

> **Патчи:** для загрузчика Allwinner вы можете найти дополнительные опциональные патчи в [**репозитории Armbian**](https://github.com/armbian/build/tree/main/patch/u-boot/u-boot-sunxi). 

## Настройка

{{#include u-boot.md}}

## Сборка

```bash
make CROSS_COMPILE=$LFA_TGT-
``` 

## Сохранение образа U-Boot

Скопируйте скомпилированный файл в директорию `$LFA` для удобного доступа к нему в будущем:

```bash
cp -v u-boot-sunxi-with-spl.bin $LFA/bootloader.bin
```

{{#include u-boot-save.md}}

~~~admonish note title="Содержимое пакета" collapsible=true
- **Установленные файлы:** `$LFA/bootloader.bin`

### Описание компонентов

- `$LFA/bootloader.bin` — скомпилированный файл загрузчика U-Boot.
~~~
