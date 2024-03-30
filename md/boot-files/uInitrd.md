# Создание uInitrd

Загрузчик U-Boot требует наличие образа `uImage`. Сначала создайте директорию, в которой будет ряд файлов из собранной системы (`$LFA_SYS`):

```bash
cd $LFA

mkdir LFA-uImage
cd LFA-uImage

cp -rv $LFA_SYS/{bin,dev,etc,lib,proc,root,sbin,srv,sys,tmp,var} .
find . | cpio -H newc -ov --owner root:root > ../initramfs.cpio

cd ..
gzip initramfs.cpio
```

Создайте образ `uImage` с помощью программы `mkimage`:

```bash
mkimage -A arm64 -T ramdisk -n uInitrd -d initramfs.cpio.gz uImage
```
