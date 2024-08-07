# linux-headers

{{#include pkgs/linux-headers.md}}

```admonish warning title="Внимание"
Обратите внимание, что исходный код `linux-headers` содержится в архиве с ядром Linux-6.6.44.
```

## Настройка

Убедитесь, что дерево исходного кода Linux чистое и не содержит лишних файлов:

```bash
make mrproper
```

## Установка

```bash
make ARCH=arm64 INSTALL_HDR_PATH=$LFA_CROSS headers_install
```

```admonish warning title="Внимание"
Обратите внимание на аргумент `ARCH=arm64`. Для 32-битных процессоров нужно заменить этот аргумент на `ARCH=arm`.

Например, если ваш процессор имеет 64-битную архитектуру (ARMv8 или ARMv8.1), то оставьте этот аргумент без изменений. Однако если у вас иная 32-битная архитектура, то замените `ARCH=arm64` на `ARCH=arm`.
```

> Если во время установки заголовков ядра (в частности, при исполнении второй команды `headers_install`) у вас возникли ошибки, проверьте, установлена ли в системе программа `rsync`.

> **Значения новых параметров:**
>
> `ARCH=arm64` — указывает `make` устанавливать заголовки для архитектуры `arm64`.
>
> `INSTALL_HDR_PATH=$LFA_CROSS` — указывает *префикс*, в который будут установлены заголовки.

~~~admonish note title="Содержимое пакета" collapsible=true
- **Установленные заголовки:** `$LFA_CROSS/include/{asm,asm-generic,drm,linux,misc,mtd,rdma,scsi,sound,video,xen}/*.h`

### Описание компонентов

- `$LFA_CROSS/include/asm/*.h` — заголовки Linux API ASM.
- `$LFA_CROSS/include/asm-generic/*.h` — общие заголовки Linux API ASM.
- `$LFA_CROSS/include/drm/*.h` — заголовки Linux DRM.
- `$LFA_CROSS/include/linux/*.h` — заголовки Linux API.
- `$LFA_CROSS/include/misc/*.h` — различные заголовки Linux API.
- `$LFA_CROSS/include/mtd/*.h` — заголовки Linux API MTD.
- `$LFA_CROSS/include/rdma/*.h` — заголовки Linux API RDMA.
- `$LFA_CROSS/include/scsi/*.h` — заголовки Linux API SCSI.
- `$LFA_CROSS/include/sound/*.h` — заголовки Linux API для работы со звуком.
- `$LFA_CROSS/include/video/*.h` — заголовки Linux API для работы с видео.
- `$LFA_CROSS/include/xen/*.h` — заголовки Linux API XEN.
~~~

---

> **Смотрите также:**
>
> - [Сборка ПО из исходного кода](../additional/compile.md);
> - [Кросс-компилятор](../additional/cross-compiler.md).
