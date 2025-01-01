# Создание boot.scr

```admonish warning title="Внимание"
Это заготовка страницы. Здесь приведены общие инструкции, тестирование которых не производилось. Окончательная версия страницы войдёт во вторую версию руководства LFA.
```

`boot.scr` — это загрузочный скрипт системы, предназначенный для U-Boot.

```bash
cat > $LFA_SYS/boot/boot.cmd << "EOF"
setenv load_addr "0x45000000"
setenv rootdev "/dev/mmcblk0p1"
setenv rootfstype "ext4"

if test "${devtype}" = "mmc"; then part uuid mmc 0:1 partuuid; fi

setenv bootargs "root=${rootdev} rootwait rootfstype=${rootfstype} ubootpart=${partuuid}"

load ${devtype} ${devnum} ${ramdisk_addr_r} ${prefix}uImage
load ${devtype} ${devnum} ${load_addr} ${prefix}/dtb-{{linux_ver}}/allwinner/sun50i-h6-orangepi-3.dtb
load ${devtype} ${devnum} ${kernel_addr_r} ${prefix}vmlinuz-{{linux_ver}}

bootz ${kernel_addr} ${initrd_addr}:${filesize} ${scriptaddr}
EOF
```

Замените `allwinner/sun50i-h6-orangepi-3.dtb` на путь до нужного файла Devicetree. Кроме того, вместо явного указания версии ядра в пути до файлов (`dtb-{{linux_ver}}`, `vmlinuz-{{linux_ver}}`) вы можете использовать ссылки (`dtb`, `vmlinuz`), которые сделали после установки ядра Linux и файлов Devicetree. Это может быть полезным, когда вы собираетесь обновлять ядро - в таком случае вам не потребуется обновлять пути в файле `boot.cmd`.

Скомпилируйте этот файл:

```bash
mkimage -C none \
  -A arm \
  -T script \
  -d $LFA_SYS/boot/boot.cmd \
  $LFA_SYS/boot/boot.scr
```
