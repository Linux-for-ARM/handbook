# linux-headers

{{#include pkgs/linux-headers.md}}

```admonish warning title="Внимание"
Обратите внимание, что исходный код `linux-headers` содержится в архиве с ядром Linux-6.6.6
```

## Настройка

Убедитесь, что дерево исходного кода Linux чистое и не содержит лишних файлов:

```bash
make mrproper
```

## Установка

```bash
make ARCH=arm64 INSTALL_HDR_PATH=$NXT_CROSS headers_install
```

> Если во время установки заголовков ядра (в частности, при исполнении второй команды `headers_install`) у вас возникли ошибки, проверьте, установлена ли в системе программа `rsync`.
