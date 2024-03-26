# libgcc

{{#include pkgs/libgcc.md}}

## Установка

Скопируйте библиотеку в директорию собираемой ОС:

```bash
cp $LFA_CROSS/lib64/libgcc_s.so.1 $LFA_SYS/lib
```

Удалите из установленной библиотеки лишние для вас отладочные символы:

```bash
$STRIP $LFA_SYS/lib/libgcc_s.so.1
```
