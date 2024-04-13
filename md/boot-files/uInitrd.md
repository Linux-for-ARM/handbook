# Создание uInitrd

```admonish warning title="Внимание"
Это заготовка страницы. Здесь приведены общие инструкции, тестирование которых не производилось. Окончательная версия страницы войдёт во вторую версию руководства LFA.
```

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

---

> **Смотрите также:**
>
> - [**Image vs zImage vs uImage (Stack Overflow)**](https://stackoverflow.com/questions/22322304/image-vs-zimage-vs-uimage)
