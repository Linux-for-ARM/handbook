Директория `configs/` содержит шаблоны конфигурационных файлов для поддерживаемых [проектом U-Boot, а не LFA] плат в соответствии со следующей схемой наименования:

```bash
<имя платы>_defconfig
```

Вы можете использовать имя одного из этих файлов в качестве цели `make` для генерации конфигурационного файла `.config`. Например, шаблон конфигурации для платы Odroid C2 называется `odroid-c2_defconfig`. Соответственно, файл `.config` генерируется командой:

```bash
make odroid-c2_defconfig
```