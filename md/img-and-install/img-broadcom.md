# Сборка образа для Broadcom

Данный раздел содержит инструкции по использованию U-Boot в SoC Broadcom 7445 и 7260 в качестве загрузчика третьего порядка, запускаемого загрузчиком BOLT компании Broadcom. BOLT загружает U-Boot как двоичный ELF-файл.

## Запуск

Чтобы указать U-Boot, какой последовательный порт использовать для консоли, установите параметр `stdout-path` в узле `/chosen` дерева устройств, сгенерированного BOLT. Например:

```bash
BOLT> dt add prop chosen stdout-path s serial0:115200n8
```

Запишите двоичный файл `$LFA/bootloader.bin` в память платы, затем вызовите его из BOLT. Например:

```bash
BOLT> boot -bsu -elf flash0.u-boot1
```

Предполагается, что I-кеш и D-кеш уже включены при входе в U-Boot.

## Запись образа системы

### Создание образа с базовой ОС

{{#include create_img.md}}

### Копирование файлов

{{#include rootfs.md}}

Теперь вам остаётся записать образ на SD- или иной носитель, с которого может загружаться компьютер.

---

> **Смотрите также:**
>
> - [**BCM7445 and BCM7260**](https://docs.u-boot.org/en/latest/board/broadcom/bcm7xxx.html) (<https://docs.u-boot.org/>);
> - [**Broadcom**](https://docs.u-boot.org/en/latest/board/broadcom/index.html);
