# musl

{{#include pkgs/musl.md}}

## Настройка

```bash
./configure CROSS_COMPILE=$LFA_TGT- \
  --prefix=/ \
  --disable-static \
  --target=$LFA_TGT
```

## Сборка

```bash
make
```

## Установка

```bash
make DESTDIR=$LFA_SYS install-libs
```

~~~admonish note title="Содержимое пакета" collapsible=true
- **Установленные программы:** `ld-musl`
- **Установленные библиотеки:** `libc.so.0`, `libcrypt.so.0`, `libdl.so.0`, `libm.so.0`, `libpthread.so.0`, `librt.so.0`

### Описание компонентов

- **Программы:**
  - `ld-musl` — динамический компоновщик/загрузчик musl.
- **Библиотеки:**
  - `libc` — библиотека языка C.
  - `libcrypt` — криптографическая библиотека.
  - `libdl` — библиотека для динамического компоновщика/зарузчика.
  - `libm` — математическая библиотека.
  - `libpthread` — библиотека потоков POSIX.
  - `librt` — библиотека часов и таймера.
~~~
